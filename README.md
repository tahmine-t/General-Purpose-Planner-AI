# General-Purpose Planner
AI Course Project  

This repository contains the implementation of a **general-purpose planner** designed for solving planning problems using state-space search methods. The project includes implementing heuristic functions, solving predefined planning domains, and analyzing the efficiency of the planner.  

---

## **Project Overview**  

The planner uses **Forward State-Space Search** to solve planning problems modeled in **PDDL (Planning Domain Definition Language)**. Two heuristics, `Preconditions Ignore` and `Delete Lists Ignore`, are implemented to optimize the search process. The planner outputs a sequence of actions leading to the goal state and calculates the time required for solving the problem.  

---

## **Features**  

### **Planner Implementation**  
- **Forward State-Space Search**: Constructs a search tree by exploring all possible actions in the state space.  
- **Heuristic Functions**:  
  - *Preconditions Ignore*: Simplifies the state evaluation by ignoring preconditions.  
  - *Delete Lists Ignore*: Focuses only on the positive effects of actions, disregarding conflicts.  
- **Action Class Methods**:  
  - `regress(state)`: Determines the regression of a state based on an action.  
  - `is_unified(state)`: Checks if the action is applicable to a given state.  
  - `is_conflicting(state)`: Evaluates if the action conflicts with the current state.  

### **Domain Modeling and Problem Solving**  
- Modeled and solved the following domains:  
  1. **Blocks World**: Rearrange blocks to achieve a goal configuration.  
  2. **Monkey and Bananas**: Navigate a monkey through actions to reach bananas.  
  3. **Depots**: Manage a depot system to transport and store goods efficiently.  
- Solved problems using both **forward** and **backward planning** approaches.  

---

## **Results**  

The planner outputs:  
1. The sequence of actions to achieve the goal state.  
2. The total time taken to solve the problem.  
