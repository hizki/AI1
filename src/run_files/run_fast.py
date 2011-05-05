from run_bfst import best_first
from run_me import run_tests
from run_files.run_beam import beam_width

def main():
    mes_funs =[best_first,beam_width]
    count= 1
    room_limit = 0.1
    run_tests(mes_funs, count, room_limit)
    
if __name__ == "__main__":
    main()