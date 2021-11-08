from typing import List

class Process:
    def __init__(self, arrival_time:int, execution_time: int) -> None:
        self.arrival_time = arrival_time
        self.execution_time = execution_time
    
    def __gt__(self, other):
        return self.execution_time > other.execution_time
    
    def __repr__(self) -> str:
        return f"<Process AT:{self.arrival_time}, ET:{self.execution_time}>"

def roundRobin(quantum: int, processes: dict[str, Process]):
    # A variable to hold the total time all the processes take to finish executing
    total_time = 0

    # A dictionary which contains the times at which the various processes execute
    executions = dict()

    while len(processes) != 0:

        for process_id, process in processes.items():
            if quantum < process.execution_time:
                process.execution_time -= quantum
                executions[f'{total_time} -> {total_time + quantum}'] = f"<Process: {process_id}>"
                total_time += quantum
            else:
                executions[f'{total_time} -> {total_time + process.execution_time}'] = f"<Process: {process_id}>"
                total_time += process.execution_time
                del processes[process_id]
                break

    return {'total_time': total_time, 'executions': executions}



if __name__ == "__main__":
    """
    Assumptions made for input format
    q: time quantum for the round robin system
    n: number of processes in the system
    next n lines: x y, where x = arrival time of processs, y = execution time of the process
    """
    quantum = int(input())
    number_of_processes = int(input())
    
    # A dictionary to hold the processes
    processes = {}

    # Collecting and storing all our processes in the dictionary
    for i in range(1, number_of_processes + 1):
        x, y = map(lambda m:int(m), input().split(" "))
        processes[f'{i}'] = Process(x, y)
    
    results = roundRobin(quantum, processes)

    print(results)
    