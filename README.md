# simulation_query

### A small python application utilising Tkinter for GUI interaction and Paramiko for SFTP to read a remote text file and, given a UUID number, return the initial conditions of the simulation with the matching UUID.

### Additional functionality added 20220510, the ability to search for a quantity and a value and return the UUIDs that match 

![](readme.gif)

The simulation database query system has three modes of working:

  Method 1) The user wants to list the values of a specific quantity across all simulations.<br>
  Method 2) The user wants to return the UUID numbers of the simulations that have a particular value assigned to a quantity<br>
  Method 3) The user wants to return the full setup of a simulation with a given UUID
  
  
