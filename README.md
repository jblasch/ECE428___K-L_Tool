<b>Project: K-L Tool</b><br>
Dates: Sep-Dec 2015<br><br>
Overview:<br>
<ul>
Software programming project to implement the Kernighan-Lin algorithm on files with nodes and edges that represent integrated circuits and their interconnects. The K-L algorithm is heuristic, so it does not find the exact solution, but will find the best solution with respect to initial conditions. In this case, the initial conditions are how the nodes are initially split, which is in half, down the middle. The graphic below illustrates the program run on a small set of data.<br><br>
K-L Tool: KL_tool_LF.py<br>
Benchmark test files (large data files):<br>
<ul><ul><ul><ul><ul><ul><ul><ul><ul><ul>
<li>add20.txt<br>
<li>bcsstk33.txt<br>
<li>data.txt<br>
<li>uk.txt<br><br> 
</ul></ul></ul></ul></ul></ul></ul></ul></ul></ul>
Input file format:</b><br><br>
<ul>
The input benchmark files are provided in the Chaco input file format. The initial (0th) line of the file contains two integers, representing the number of nodes and the number of edges in the graph. Each following (nth) line contains the list of nodes that share an edge with the nth node, separated by spaces.<br>

<ul><ul>
The following example represents a complete graph on 6 vertices in this format.<br> 
6 15<br>
23456<br>
13456<br>
12456 12356 12346 12345<br>
</ul></ul></ul>

<img src="http://i68.tinypic.com/2lm6gw2.jpg" border="0" alt="Small file output"></a>
