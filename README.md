# Dots-and-Boxes
from: http://www.math.ucla.edu/~tom/Games/dots&boxes_hints.html


Some Strategy For Dots and Boxes
In the game of Dots and Boxes, the winner is generally the player who makes the last move. The reason for this is that at the end of the game, there are usually a few long corridors or chains of boxes left to be taken. If your opponent is forced to play in one of these chains, then you can take all but two of the boxes and, by sacrificing the last two boxes, make certain that it is his turn to play into the next long chain. You will thus win all but two boxes in each long chain, and of course you will win all boxes in the last chain. We say a chain is long if it contains at least three boxes.
The above program for playing Dots and Boxes uses an algorithm that is not very good, but it will play well once there are only long chains left. You may use it to improve your play at the next level of understanding. This next level requires determining which player will move last. This is most usefully done using the following rule.

The Long Chain Rule: Suppose the playing field is a rectangle of m rows and n columns and so has mn boxes. If both m and n are even, then the first player should play to make the number of long chains odd. If either m or n is odd, then the first player should play to make the number of long chains even.

Of course then the second player wants an even number of long chains if both m and n are even, and an odd number of long chains otherwise.

It must be pointed out that in this rule, loops do not count as long chains.

Here is the reason this rule works. There are (m+1)n horizontal edge moves and m(n+1) vertical edge moves for a total of 2mn+m+n moves. Without the rule that the player who completes a box moves again, we could say that the player who moves first also moves last if and only if 2mn+m+n is odd.
With the rule that the player who completes a box moves again, we must subtract one for each time at least one box is filled, except for the last box. Some moves complete two boxes simultaneously. Let us call these moves double-box moves. If there are no double-box moves, then since there are mn boxes and since completing the last box doesn't change things, we must subtract mn-1 from the total number of moves to get the number of move changes. This gives 2mn+m+n-(mn-1)=mn+m+n+1=(m+1)(n+1). Thus if there are no double-box moves, then the player who moves first also moves last if and only if (m+1)(n+1) is odd. The same is therefore true if there is an even number of double-box moves in the game.

Another way of putting this is to say that if (and only if) (m+1)(n+1) is odd, the first player wants to arrange things so that there is an even number of double-box moves in the game. For a chain of length 1 or 2, neither player need allow a double-box move to be made. However, in each chain of length 3 or more, either player may take all boxes but two, providing the opponent with a single double-box move. For a loop of four or more boxes, either player may take all but four boxes, providing the opponent with two double-box moves. Thus, in a well played game, the number of double-box moves is equal to the number of long chains, plus twice the number of loops, minus one because the player to move in the last long chain will take all of the boxes. So if (m+1)(n+1) is odd, the first player wants an odd number of long chains in the game. Moreover, (m+1)(n+1) is odd if and only if both m and n are even.

To go beyond this level of understanding of the game, read the book of Berlekamp.
