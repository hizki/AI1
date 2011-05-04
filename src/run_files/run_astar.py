from measurments import beam
import run_me

def main():
    mes_funs =[beam]
    rooms_count= 10
    room_limit = 50.0
    
    run_me.run_tests(mes_funs, rooms_count, room_limit)
    

if __name__ == "__main__":
    main()