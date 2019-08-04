<p align="center">
<img src = "https://user-images.githubusercontent.com/40419750/59024126-d9996680-886e-11e9-8af9-1084288699f2.png" width=100 height=100>
</p>

<h1 align="center">pingpongAI</h1>
<div align="center">
<img src="https://img.shields.io/github/license/sushantPatrikar/pingpongAI">	
<img src="https://www.codefactor.io/repository/github/sushantpatrikar/pingpongai/badge/master"/>
<img src="https://img.shields.io/github/issues-pr/sushantPatrikar/pingpongAI">
<img src="https://img.shields.io/github/stars/sushantPatrikar/pingpongAI">
<img src="https://img.shields.io/github/forks/sushantPatrikar/pingpongAI">
<img src="https://img.shields.io/github/issues/sushantPatrikar/pingpongAI">
<img src="https://img.shields.io/badge/PRs-welcome-informational">
</div>

<h4 align="center">Ping Pong game, but AI plays it</h4>
<hr>
<p align="center">
<img src = "./genetic gifs/gen20.gif" height=400 width=600>
</p>

<h4 align="center">AI plays Ping Pong using Neuroevolution of Augmenting Topologies(NEAT)</h4>

Every generation starts with the population of 200 bars. Every bar has it's own corressponding ball. The aim is to protect the ball from falling down. Once all the bars are dead, next generation is generated. For every 200 individuals of next generation 2 parents are selected from the previous genertion. The selected two parents are crossovered, followed by some percentage of mutation(generally low %).

Every bar looks in 5 direction:

<p align="center">
  <img src = "./genetic screenshots/QI.png" height=300 width=300>
  
  It's distance from the ball in Quadrant I, relative to it's positon and ball's velocity(If it is present in Quadrant I)
</p>

<p align="center">
  <img src = "./genetic screenshots/QII.png" height=300 width=300>
  
  It's distance from the ball in Quadrant II, relative to it's positon and ball's velocity(If it is present in Quadrant II)
</p>

<p align="center">
  <img src = "./genetic screenshots/Straight.png" height=300 width=300>
  
  It's distance from the ball in straight direction, relative to it's positon, and ball's velocity(If it is present overhead)
</p>

<p align="center">
  <img src = "./genetic screenshots/wall1.png" height=80 width=600>
  
  It's distance from the left wall.
</p>

<p align="center">
  <img src = "./genetic screenshots/wall2.png" height=80 width=600>
  
  It's distance from the right wall.
</p>


Initial generation looks like this
<p align="center">
<img src = "./genetic gifs/gen2.gif" height=400 width=600>
</p>

Initially, the bars have no clue, these are just random decisions i.e Move Right or Move Left

After some generations we see some improvements:
<p align="center">
<img src = "./genetic gifs/gen6.gif" height=400 width=600>
</p>
By this generation the bars start taking some sensible decisions

<br>
<p>As the generations go on, the AI becomes master in playing this game</p>
<p align="center">
<img src = "./genetic gifs/gen20.gif" height=400 width=600>
</p>
<p>For detailed explanation, you can visit my <a href="https://sushantpatrikar.github.io/flappybirdAI.html"> website</a>.</p>


<p>For human playable version of this game, Click <a href="https://github.com/sushantPatrikar/pingpong">here</a></p>

<h2>Future Scope</h2>
<p>Right now, the algorithm used is NEAT. Some other Reinforcement Learning algorithm, such as Deep Q-Learning can be applied to it. If you have any other ideas, Pull Requests are welcomed!</p>
