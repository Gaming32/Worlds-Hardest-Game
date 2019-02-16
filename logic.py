
import tkinter as tk#; from tkinter.constants import *
import tkinter.simpledialog as simpledialog
import tkinter.filedialog as filedialog
from tkinter.messagebox import showinfo, showwarning, showerror
from python_tools.matrices import *
from enum import Enum

win = tk.Tk()

class objtypes(Enum):
    Nothing='white'
    Ground='grey'
    Start='red'
    Safe='yellow'
    Goal='green'
def getlvlinfo(btnmatrix):
    res = []
    for (i, column) in enumerate(btnmatrix):
        res.append([])
        for btn in column:
            res[i].append(objtypes(btn.cget('bg')))
    return res
def switchlvlinfo(obj):
    if obj==objtypes.Nothing: obj=objtypes.Ground
    elif obj==objtypes.Ground: obj=objtypes.Start
    elif obj==objtypes.Start: obj=objtypes.Safe
    elif obj==objtypes.Safe: obj=objtypes.Goal
    elif obj==objtypes.Goal: obj=objtypes.Nothing
    return obj
def setlvlinfo(colmatrix, btnmatrix):
    for (x, column) in enumerate(btnmatrix):
        for (y, btn) in enumerate(column):
            btn.config(bg=colmatrix[x][y].value)
def changebtncolor(btn):
    btn.config(bg=switchlvlinfo(objtypes(btn.cget('bg'))).value)

def config(matrix):
    matrix = getlvlinfo(matrix)
    data = 'function setTiles() {'
    for (obj, x, y) in getmatrixobjs(matrix):
        if obj == objtypes.Start:
            data += 'playerPos = createVector(%s, %s);' % (x,y)
        if obj == objtypes.Ground: pass
        else:
            data += 'tiles[%s][%s].' % (x, y)
            if obj == objtypes.Safe or obj == objtypes.Start: val = 'safe'
            elif obj == objtypes.Goal: val = 'goal'
            else: val = 'wall'
            data += '%s = true;' % val
    data += '}'
    return settings % data
import os
def spawn(conf):
    open('level/level.html', 'w').write(html)
    open('level/PlayerLvlFinal.js', 'w').write(code)
    open('level/setting_level.js', 'w').write(conf)

code = """
class Player{constructor(){this.pos=createVector(playerPos.x*tileSize+tileSize/4+xoff,playerPos.y*tileSize+tileSize/4+yoff);this.vel=createVector(0,0);this.size=tileSize/2.0;this.playerSpeed=tileSize/15.0;this.dead=false;this.reachedGoal=false;this.fadeCounter=255;this.isBest=false;this.deathByDot=false;this.deathAtStep=0;this.moveCount=0;this.gen=1;this.fitness=0;this.nodes=[];this.fading=false;this.brain=new Brain(numberOfSteps);this.human=false;this.coins=[];this.setCoins();this.setNodes();this.nextNode=0;this.directionToGo=createVector(1,0);this.sameAsTopTil=0;this.winsinsteps=100000;}
setCoins(){}
setNodes() {
    this.nodes[0] = new Node(createVector(955, 85), false, false);
    this.nodes[1] = new Node(createVector(955, 535), false, false);
    this.nodes[2] = new Node(createVector(305, 535), false, false);
    this.nodes[3] = new Node(createVector(305, 185), false, false);
    this.nodes[4] = new Node(createVector(855, 185), false, false);
    this.nodes[5] = new Node(createVector(855, 435), false, false);
    this.nodes[6] = new Node(createVector(405, 435), false, false);
    this.nodes[7] = new Node(createVector(405, 285), false, false);
    this.nodes[8] = new Node(createVector(755, 310), false, false);
    this.nodes[7].setDistanceToFinish(this.nodes[8]);
    this.nodes[6].setDistanceToFinish(this.nodes[7]);
    this.nodes[5].setDistanceToFinish(this.nodes[6]);
    this.nodes[4].setDistanceToFinish(this.nodes[5]);
    this.nodes[3].setDistanceToFinish(this.nodes[4]);
    this.nodes[2].setDistanceToFinish(this.nodes[3]);
    this.nodes[1].setDistanceToFinish(this.nodes[2]);
    this.nodes[0].setDistanceToFinish(this.nodes[1]);
  }
//%s
show(){if(!this.isBest&&this.sameAsTopTil>this.brain.step){return;}
fill(255,0,0,this.fadeCounter);if(this.isBest&&!showBest){fill(0,255,0,this.fadeCounter);}
stroke(0,0,0,this.fadeCounter);strokeWeight(4);rect(this.pos.x,this.pos.y,this.size,this.size);stroke(0);for(var i=0;i<this.coins.length;i++){this.coins[i].show();}}
move(bestPlayer){if(!humanPlaying){if(!this.isBest&&this.sameAsTopTil>=bestPlayer.brain.step){if(bestPlayer.dead||bestPlayer.reachedGoal){this.dead=bestPlayer.dead;this.deathByDot=bestPlayer.deathByDot;this.reachedGoal=bestPlayer.reachedGoal;for(var i=0;i<bestPlayer.nodes.length;i++){this.nodes[i].reached=bestPlayer.nodes[i].reached;}
for(var i=0;i<bestPlayer.coins.length;i++){this.coins[i].taken=bestPlayer.coins[i].taken;}
return;}else if(this.sameAsTopTil==bestPlayer.brain.step){this.pos=bestPlayer.pos.copy();this.brain.step=bestPlayer.brain.step;for(var i=0;i<bestPlayer.nodes.length;i++){this.nodes[i].reached=bestPlayer.nodes[i].reached;}
for(var i=0;i<bestPlayer.coins.length;i++){this.coins[i].taken=bestPlayer.coins[i].taken;}}else{return;}}
if(this.moveCount==0){if(this.brain.directions.length>this.brain.step){this.vel=this.brain.directions[this.brain.step];this.brain.step++;}else{this.dead=true;this.deathAtStep=this.brain.step;this.fading=true;}
this.moveCount=10;}else{this.moveCount--;}}
showCount++;var temp=createVector(this.vel.x,this.vel.y);temp.normalize();temp.mult(this.playerSpeed);for(var i=0;i<solids.length;i++){temp=solids[i].restrictMovement(this.pos,createVector(this.pos.x+this.size,this.pos.y+this.size),temp);}
this.pos.add(temp);}
checkCollisions(){if(!this.isBest&&this.sameAsTopTil>this.brain.step){return;}
for(var i=0;i<this.coins.length;i++){this.coins[i].collides(this.pos,createVector(this.pos.x+this.size,this.pos.y+this.size));}
for(var i=0;i<dots.length;i++){if(dots[i].collides(this.pos,createVector(this.pos.x+this.size,this.pos.y+this.size))){this.fading=true;this.dead=true;this.deathByDot=true;this.deathAtStep=this.brain.step;}}
this.reachedGoal=true;if(!winArea.collision(this.pos,createVector(this.pos.x+this.size,this.pos.y+this.size))){this.reachedGoal=false;}else{for(var i=0;i<this.coins.length;i++){if(!this.coins[i].taken){this.reachedGoal=false;break;}}}
for(var i=0;i<this.nodes.length;i++){if(!this.nodes[i].reached){this.nodes[i].collision(this.pos,createVector(this.pos.x+this.size,this.pos.y+this.size));break;}}
if(this.reachedGoal){this.winsinsteps=this.brain.step;}}
update(bestPlayer){if(!this.dead&&!this.reachedGoal){this.move(bestPlayer);this.checkCollisions();}else if(this.fading){if(this.fadeCounter>0){if(humanPlaying||replayGens){this.fadeCounter-=10;}else{this.fadeCounter=0;}}}}
calculateFitness(){if(this.reachedGoal){this.fitness=1.0/16.0+10000.0/(this.brain.step*this.brain.step);}else{var estimatedDistance=0.0;for(var i=this.nodes.length-1;i>=0;i--){if(!this.nodes[i].reached){estimatedDistance=this.nodes[i].distToFinish;estimatedDistance+=dist(this.pos.x,this.pos.y,this.nodes[i].pos.x,this.nodes[i].pos.y);}}
this.fitness=1000000.0/(estimatedDistance*estimatedDistance*estimatedDistance*estimatedDistance*estimatedDistance*estimatedDistance);if(this.deathByDot){this.fitness=0;}}
this.fitness*=this.fitness;for(var i=0;i<this.coins.length;i++){if(this.coins[i].taken){this.fitness*=1.2;}}}
gimmeBaby(){var baby=new Player();baby.brain=this.brain.clone();baby.deathByDot=this.deathByDot;baby.deathAtStep=this.deathAtStep;baby.gen=this.gen;for(var i=0;i<this.nodes.length;i++){if(!this.nodes[i].reached){baby.nextNode=i;break;}}
baby.directionToGo=this.nodes[baby.nextNode].pos.copy();baby.directionToGo.x-=this.pos.x;baby.directionToGo.y-=this.pos.y;baby.directionToGo.normalize();baby.directionToGo.x=round(baby.directionToGo.x*100)/100;baby.directionToGo.y=round(baby.directionToGo.y*100)/100;baby.winsinsteps=this.winsinsteps;return baby;}
mutate(died,deathStep){this.brain.mutate(died,deathStep,this.directionToGo);}
setSameAsTopTil(topBrain){this.sameAsTopTil=this.brain.directions.length;for(var i=0;i<this.brain.directions.length;i++){if(!(topBrain.directions[i].x==this.brain.directions[i].x&&topBrain.directions[i].y==this.brain.directions[i].y)){this.sameAsTopTil=i;return;}}}}
"""
settings = """
function setValues(){increaseEvery=2;increaseMovesBy=5;populationSize=1000;}
%s
function setDots(){}
function setEdges(){for(var i=0;i<tiles.length;i++){for(var j=0;j<tiles[0].length;j++){tiles[i][j].edges=[];if(tiles[i][j].wall){if(i!=tiles.length-1&&!tiles[i+1][j].wall){tiles[i][j].edges.push(1);}
if(j!=tiles[0].length-1&&!tiles[i][j+1].wall){tiles[i][j].edges.push(2);}
if(i!=0&&!tiles[i-1][j].wall){tiles[i][j].edges.push(3);}
if(j!=0&&!tiles[i][j-1].wall){tiles[i][j].edges.push(4);}}}}}
function setSolids(){var tlTile;var brTile;solids=[];for(var i=0;i<tiles.length;i++){for(var j=0;j<tiles[0].length;j++){tiles[i][j].isInSolid=false;}}
var edgeNumber=0;for(var i=0;i<tiles.length;i++){for(var j=0;j<tiles[0].length;j++){if(tiles[i][j].edges.length>0&&!tiles[i][j].isInSolid){var rightFound=true;var downFound=true;tlTile=tiles[i][j];tlTile.isInSolid=true;var i2=i+1;while(i2<tiles.length&&tiles[i2][j].edges.length>0){tiles[i2][j].isInSolid=true;i2++;}
brTile=tiles[i2-1][j];if(i2-1!=i){solids.push(new Solid(tlTile,brTile));}else{rightFound=false;}
var j2=j+1;while(j2<tiles[0].length&&tiles[i][j2].edges.length>0){tiles[i][j2].isInSolid=true;j2++;}
brTile=tiles[i][j2-1];if(j2-1!=j){solids.push(new Solid(tlTile,brTile));}else{if(!rightFound){solids.push(new Solid(tlTile,brTile));}
downFound=false;}}}}
for(var i=0;i<solids.length;i++){console.log(solids[i]);}}
function setWinArea(){var tl=tiles[0][0];var firstTl=true;var br=tiles[0][0];for(var i=0;i<tiles.length;i++){for(var j=0;j<tiles[0].length;j++){if(tiles[i][j].goal){if(firstTl){tl=tiles[i][j];firstTl=false;}
br=tiles[i][j];}}}
winArea=new Solid(tl,br);}
"""
html = """
<html><head><meta charset="UTF-8"><script language="javascript" type="text/javascript" src="../libraries/p5.js"></script><script language="javascript" src="../libraries/p5.dom.js"></script><script language="javascript" src="../libraries/p5.sound.js"></script><script language="javascript" type="text/javascript" src="../sketch.js"></script><script language="javascript" type="text/javascript" src="../Tile.js"></script><script language="javascript" type="text/javascript" src="PlayerLvlFinal.js"></script><script language="javascript" type="text/javascript" src="setting_level.js"></script><script language="javascript" type="text/javascript" src="../Solid.js"></script><script language="javascript" type="text/javascript" src="../Dot.js"></script><script language="javascript" type="text/javascript" src="../Population.js"></script><script language="javascript" type="text/javascript" src="../Brain.js"></script><script language="javascript" type="text/javascript" src="../Node.js"></script><script language="javascript" type="text/javascript" src="../Coin.js"></script><link rel ="stylesheet" type = "text/css" href="../../../../style.css"/><link rel ="stylesheet" type = "text/css" href="../localStyle.css"/><link rel = "shortcut icon" type = "image/png" href = "../../../../img/favicon3.png"/><title> TheBigCB.com </title></head><body><div id="container"><div id="header"><h1> TheBigCB.com </h1><h6> Because CodeBullet.com was taken</h6></div><hr><div id = "main"><h2> Worlds Hardest Game Remake</h2><div id = "canvas"></div><br/><div id = "instructions">P -> play yourself &emsp;&emsp; G -> replay evolution hightlights &emsp;&emsp; SPACE -> only show best player</div><br/><div id = buttons><div id = "resetButton"></div><br/><hr/><br/><div id = "popSize"></div><br/><div id = "mutationRate"></div><br/><div id = "evolutionSpeed"></div><br/><hr/><div id = "increaseMovesBy"></div><br/><div id = "increaseEvery"></div><br/></div></div></div><script>
    //center the canvas
    var tempString = ""+((window.innerWidth*0.9- 1306 - window.innerWidth*0.9*0.08 )/2)+ "px";
    document.getElementById("main").style.marginLeft = tempString;


    window.onresize = function(event) {
      var tempString = ""+((window.innerWidth*0.9- 1306 - window.innerWidth*0.9*0.08 )/2)+ "px";
      document.getElementById("main").style.marginLeft = tempString;
    };

  </script></body></html>
"""