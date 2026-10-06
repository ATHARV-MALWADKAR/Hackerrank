# [Far Vertices](https://www.hackerrank.com/challenges/far-vertices/problem?isFullScreen=true)
## Hard
<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>You are given a tree that has N vertices and N-1 edges. Your task is to mark as small number of vertices as possible, such that, the maximum distance between two unmarked vertices is less than or equal to K. Output this value.
Distance between two vertices i and j is defined as the minimum number of edges you have to pass in order to reach vertex i from vertex j.  </p>

<p><strong>Input Format</strong> <br>
The first line of input contains two integers N and K. The next N-1 lines contain two integers (ui,vi) each, where 1 &lt;= ui,vi &lt;= N. Each of these lines specifies an edge. <br>
N is no more than 100. K is less than N.  </p>

<p><strong>Output Format</strong> <br>
Print an integer that denotes the result of the test.</p>

<p><strong>Sample Input:</strong></p>

<pre><code>5 1  
1 2  
1 3  
1 4  
1 5
</code></pre>

<p><strong>Sample Output:</strong></p>

<pre><code>3
</code></pre>

<p><strong>Sample Input:</strong></p>

<pre><code>5 2  
1 2  
1 3  
1 4  
1 5
</code></pre>

<p><strong>Sample Output:</strong></p>

<pre><code>0
</code></pre>

<p><strong>Explanation:</strong></p>

<p>In the first case you have to mark at least 3 vertices, and in the second case you don't need to mark any vertices.</p></div></div></div></div>