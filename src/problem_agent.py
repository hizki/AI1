NO_LIMIT = -1

class ProblemAgent ():
    '''
    This is an interface for a Problem Solving Agent.
    '''
    
    def solve(self, problem_state, time_limit = NO_LIMIT):
        '''
        This is the method called by the runner of this agent.
        It includes the code that solves the problem.
        
        @param problem_state: Initial problem state.
        @param time_limit: The time limit for this agent.
        @return: A list of ProblemActions that solves the given problem.
        '''
        raise NotImplementedError()
