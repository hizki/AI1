# -*- coding:utf-8 -*-
"""
Created on Apr 30, 2011

@author: inesmeya
"""
import pylab as P
import os
    
def plot_result(result,title=None, label=None, filename=None, show=False):
    ''' Plots graph for result
        shows graph if  filename is not present
        saves to file if filename is present
        @param result: as ((x_name, x),(y_name, y))
    '''
    ((x_name, x),(y_name, y)) = result
    
    P.title(title)
    P.xlabel(x_name)
    P.ylabel(y_name)

    
    #P.figtext(0, 0.8, 'foo')
    P.plot(x,y, label=label)
    P.legend(loc='lower right')

    
    if filename is not None:
        P.savefig(filename)
    else:
        if show==True:P.show()
    



class TableTemplate():
    
    def _cell_tmpl(self,cell):
        return '''
          <td>{cell}</td>
        '''.format(cell=cell)
        
    def _row_tmpl(self,row_body):
        return '''
            <tr> 
              {row_body}
            </tr>
        '''.format(row_body=row_body)
    
    def _table_tmpl(self,title,header_body,body):
        return '''
            <div style="padding-left:80px;  border:#000000 1px;">
            <table>
              <!-- Title -->
              <tr>
                <th colspan="3"> {title} </th>
              </tr>
              <!-- Header -->
              <tr class="yellow"> 
                {header_body}
              </tr>
              <!-- Body -->
              {body}
            </table>
            </div>
        '''.format(title=title, header_body=header_body, body=body)
    

    def _html_row(self,row_body):
        return self._row_tmpl.format(row=row_body)
    
    def _make_row_body(self, row): 
        html_cell_list = [ self._cell_tmpl(cell) for cell in row]
        row_body = ' '.join(html_cell_list)
        return row_body
    
    def _make_table_body(self,table):
        html_row_body_list = [self._make_row_body(row) for row in table]
        html_row_list      = [self._row_tmpl(row_body) for row_body in html_row_body_list]
        table_body = ' '.join(html_row_list)
        return table_body
    
    def make_html_table(self,table,title,header=None, vertical=False):
        
        if vertical:
            table = zip(*table)
            
        if header is not None: table = [header] + table
        
        header_row = table[0]
        body_rows =  table[1:]
        
        header_body = self._make_row_body(header_row)
        body = self._make_table_body(body_rows)
        
        html_table = self._table_tmpl(title, header_body, body)
        return html_table
        
    
def table_to_html(table,title,header=None):
    '''Converts table to html string representation
    @param table: [ [column headers list], [row1 list],[row2 list]...]
    @param title: string for title
    '''      
    return TableTemplate().make_html_table(table, title,header=header)     

  

def table_to_csv(table):
    rows   = [', '.join(map(str,row)) for row in table]
    result = '\n'.join(rows)
    return result
        
def table_to_csv2(table,header=None):
    
    tr_table = zip(*table)
    if header is not None: tr_table = [header] + tr_table
    result = table_to_csv(tr_table)
    return result

def test_table_to_csv():
    table = [
        ['Graphs', 'BFS', 'DFS'],
        ['#1', 10, 15],
        ['#2', 3, 17],
        ['#3', 6, 12]
    ]
    #template = TableTemplate()
    result = table_to_csv(table)
    print result    

    
def test_table_to_html():
    #table = [ ('a', 'b'), (1, 10), (2, 20), (3, 30)]
    table = [
        ['Graphs', 'BFS', 'DFS'],
        ['#1', 10, 15],
        ['#2', 3, 17],
        ['#3', 6, 12]
    ]
    #template = TableTemplate()
    result = table_to_html(table, 'ttt')
    print result
    


class HtmlFile():
    def __init__(self):
        self.content = []
        self.header ='''
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml">
    
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>Rumba Report</title>
            <style type="text/css">
            <!--
            @import url("style.css");
            -->
            </style>
            </head>
            <body>
        '''
        self.footer = '''
            </body>
            </html>
        '''
        
    def add_paragraph(self,p):
        self.content.append("<p> %s </p>\n" % p) 
    
    def add_img(self,filename):
        self.content.append(
        '<img width="600" src="{0}" alt="{0}" /> '.format(filename) )
        
    
    def add_table(self,table,title,header=None):
        self.content.append( table_to_html(table,title,header=header) )
    
    def add_header(self,h):
        self.content.append("<h2> %s </h2>\n" % h) 
    
    def save(self,filename_path):
        page = [self.header] + self.content + [self.footer]
        with open(filename_path,'w+') as file: file.writelines(page)
        self.content = []

    def save_wd(self,filename):
        filename_path = os.path.join(self.wdir,filename)
        self.save(filename_path)
    
    def set_working_dir(self,path):
        self.wdir = path
    
    def plot_result(self,result,title=None, label=None, filename=None):
        filename_path = os.path.join(self.wdir,filename)
        plot_result(result, title, label)
        self.add_img(filename)

    def plot(self,result,title=None, label=None):
        plot_result(result, title, label)
            
    def add_img_plot(self,filename):
        filename_path = os.path.join(self.wdir,filename)
        P.savefig(filename_path)
        self.add_img(filename)       
        
    
html = HtmlFile()