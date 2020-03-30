<h1>Notice</h1>

<p> Due to the high volume of students downloading my code to use on school projects, I have temporarily taken down files which contain my code, until further notice. I encourage fellow students to write their own code. You can still compare the output of your code to the output of mine by running the testbench files I have included in this repository on your code. You can compare the outputs of your code to the output results of mine that I have uploaded to this repository.
    </p>
<p>
Thank you for your understanding on this matter.
    </p>

<h1>Project: K-L Tool</h1>
Dates: Sep-Dec 2015<br /><br />
<b>Overview:</b><br>
<ul>
<p>Software programming project to implement the Kernighan-Lin algorithm on files with nodes and edges that represent integrated circuits and their interconnects. The K-L algorithm is heuristic, so it does not find the exact solution, but will find the best solution with respect to initial conditions. In this case, the initial conditions are how the nodes are initially split, which is in half, down the middle. The graphic below illustrates the program run on a small set of data.</p>
<i>K-L Tool</i>: KL_tool_LF.py<br />
<i>Benchmark test files</i> (large data files):<br />
<ul>
<li>add20.txt</li>
<li>bcsstk33.txt</li>
<li>data.txt</li>
<li>uk.txt</li>
</ul></ul>
<b>Input file format:</b><br />
<ul>
The input benchmark files are provided in the Chaco input file format. The initial (0th) line of the file contains two integers, representing the number of nodes and the number of edges in the graph. Each following (nth) line contains the list of nodes that share an edge with the nth node, separated by spaces.<br><br>


The following example represents a complete graph on 6 vertices in this format.<br> 
<ul>
6 15<br>
2 3 4 5 6<br/>
1 3 4 5 6<br/>
1 2 4 5 6<br/> 
1 2 3 5 6<br/> 
1 2 3 4 6<br/>
1 2 3 4 5<br/>
</ul></ul>

<!-- Tinypic is defunkt. Trying to find a work around -->

<!-- <img src=" https://drive.google.com/open?id=1G51kip9KbaEJ42SqCmernI7kc79WiGii "></a> -->
<!--<img src="https://drive.google.com/uc?export=view&id=XXX">-->
<!-- <img src="https://drive.google.com/uc?export=view&id=1G51kip9KbaEJ42SqCmernI7kc79WiGii"> -->
<!-- https://drive.google.com/file/d/1SLDITOhdqLeMxSIqK-2tufjPEP6l17L3/view -->


<!-- <a href="https://drive.google.com/uc?export=view&id=1SLDITOhdqLeMxSIqK-2tufjPEP6l17L3">
    <img src="https://drive.google.com/uc?export=view&id=1SLDITOhdqLeMxSIqK-2tufjPEP6l17L3"
    style="width: 100px; max-width: 50%; height: auto"
    title="Click for the larger version." />
</a> -->

<a href="https://drive.google.com/uc?export=view&id=1npfpf69UQrBB76hj6qQ8qeFLJzPDh3i7">
    <img src="https://drive.google.com/uc?export=view&id=1npfpf69UQrBB76hj6qQ8qeFLJzPDh3i7"
    width="600" height="auto"
    title="Click for the larger version." />
</a>
<br><br>

Output on a slightly more complicated data set:<br/><br/>
<a href="https://drive.google.com/uc?export=view&id=1UjP4iCq6nP7PerSegjcP6aB3XotYDlyG">
    <img src="https://drive.google.com/uc?export=view&id=1UjP4iCq6nP7PerSegjcP6aB3XotYDlyG"
    width="800" height="auto"
    title="Click for the larger version." />
