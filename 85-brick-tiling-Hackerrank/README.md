# [Brick Tiling](https://www.hackerrank.com/challenges/brick-tiling/problem?isFullScreen=true)
## Hard
<div class="challenge-body-html"><div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>You are given a grid having N rows and M columns. A grid square can either be blocked or empty. Blocked squares are represented by a '#' and empty squares are represented by '.'. Find the number of ways to tile the grid using L shaped bricks. A L brick has one side of length three units while other of length 2 units. All empty squares in the grid should be covered by exactly one of the L shaped tiles, and blocked squares should not be covered by any tile. The bricks can be used in any orientation (they can be rotated or flipped).</p></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>The first line contains the number of test cases <em>T</em>. <em>T</em> test cases follow. Each test case contains <em>N</em> and <em>M</em> on the first line, followed by <em>N</em> lines describing each row of the grid.</p></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>1 &lt;= <em>T</em> &lt;= 50 <br>
1 &lt;= <em>N</em> &lt;= 20 <br>
1 &lt;= <em>M</em> &lt;= 8 <br>
Each grid square will be either '.' or '#'.</p></div></div></div><div class="challenge_output_format"><div class="msB challenge_output_format_title"><p><strong>Output Format</strong></p></div><div class="msB challenge_output_format_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p>Output the number of ways to tile the grid. Output each answer modulo 1000000007.</p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre><code>3  
2 4  
....  
....  
3 3  
...  
.#.  
...  
2 2  
##  
##
</code></pre></div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><pre><code>2  
4  
1
</code></pre></div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><svg style="display: none;"><defs id="MathJax_SVG_glyphs"></defs></svg><p><strong>NOTE:</strong> <br>
If all points in the grid are blocked the number of ways is 1, as in the last sample testcase.</p></div></div></div></div>