## Jackson Algorithm with Python

Python's Implementation of a flow shop scheduling algorithm (JACKSON) (N tasks on M machines): CDS heuristic.

# Earliest Due Date (EDD) 

EDD is algorithm proposed by Jackson in 1955 : 

- Jackson proposed a EDD (Earliest Due Date) algorithm in 1995 that minimizes the maximum lateness of above given task model.
EDD says that, given a set of n independent tasks, any algorithm that executes the tasks in order of nondecreasing deadlines is optimal respect to minimizing the maximum lateness.

- The definition of maximum lateness is the maximum value among n task’s finish time minus its deadline.

- If a task set consists of n tasks, the schedulability condition can be perfomed by verifying the following n conditions.

![](https://github.com/timotito/Algo_Cds_Ordanncement/blob/master/output/ImagesOutput/output_diagram_gantt(1).png?raw=true)
