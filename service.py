import multiprocessing
import elements 

def main_servie(jobs, environment):
    print("AIRPLANE FLIGHT SIMULATOR")
    user_input = input("Do You want to go flying?\n\r")
    while user_input in ['y', 'yes']:
        print("\nNew Flight")
        process = multiprocessing.Process(target = environment.run(user_input))
        jobs.append(process)
        user_input = input("\nDo you want to fly again?\n\r")

    print("\nSee You next time")   
