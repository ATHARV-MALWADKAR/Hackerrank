# [Extremum Permutations](https://www.hackerrank.com/challenges/extremum-permutations/problem?isFullScreen=true)
## Medium
<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>Let's consider a permutation <em>P = {p<sub>1</sub>, p<sub>2</sub>, ..., p<sub>N</sub>}</em> of the set of <em>N = {1, 2, 3, ..., N}</em> elements .  </p>

<p><em>P</em> is called a magic set if it satisfies both of the following constraints:  </p>

<ul>
<li>Given a set of <em>K</em> integers, the elements in positions <em>a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>K</sub></em> are less than their adjacent elements, i.e., <em>p<sub>a<sub>i</sub>-1</sub> &gt; p<sub>a<sub>i</sub></sub> &lt; p<sub>a<sub>i</sub>+1</sub></em></li>
<li>Given a set of <em>L</em> integers, elements in positions <em>b<sub>1</sub>, b<sub>2</sub>, ..., b<sub>L</sub></em> are  greater than their adjacent elements, i.e., <em>p<sub>b<sub>i</sub>-1</sub> &lt; p<sub>b<sub>i</sub></sub> &gt; p<sub>b<sub>i</sub>+1</sub></em></li>
</ul>

<p>How many such magic sets are there?</p>

<p><strong>Input Format</strong> <br>
The first line of input contains three integers <em>N</em>, <em>K</em>, <em>L</em> separated by a single space. <br>
The second line contains <em>K</em> integers, <em>a<sub>1</sub>, a<sub>2</sub>, ... a<sub>K</sub></em> each separated by single space. <br>
the third line contains <em>L</em> integers, <em>b<sub>1</sub>, b<sub>2</sub>, ... b<sub>L</sub></em> each separated by single space. </p>

<p><strong>Output Format</strong> <br>
Output the answer modulo 1000000007 (10<sup>9</sup>+7).</p>

<p><strong>Constraints</strong> <br>
3 &lt;= <em>N</em> &lt;= 5000 <br>
1 &lt;= K, L &lt;= 5000 <br>
2 &lt;= a<sub>i</sub>, b<sub>j</sub> &lt;= N-1, where i ∈ [1, K] AND j ∈ [1, L]  </p>

<p><strong>Sample Input #00</strong>  </p>

<pre><code>4 1 1
2
3
</code></pre>

<p><strong>Sample Output #00</strong>  </p>

<pre><code>5
</code></pre>

<p><strong>Explanation #00</strong></p>

<p>Here, N = 4 a<sub>1</sub> = 2 and b<sub>1</sub> = 3. The 5 permutations of {1,2,3,4} that satisfy the condition are </p>

<ul>
<li>2 1 4 3</li>
<li>3 2 4 1</li>
<li>4 2 3 1</li>
<li>3 1 4 2</li>
<li>4 1 3 2</li>
</ul>

<p><strong>Sample Input #01</strong></p>

<pre><code>10 2 2
2 4
3 9
</code></pre>

<p><strong>Sample Output #01</strong></p>

<pre><code>161280
</code></pre></div></div></div></div>