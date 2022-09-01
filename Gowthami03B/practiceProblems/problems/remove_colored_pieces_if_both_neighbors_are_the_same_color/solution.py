class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_count = bob_count =0 
        for i in range(2,len(colors)):
            if colors[i-2] == 'A' and colors[i-1] == 'A' and colors[i] == 'A':
                alice_count += 1
            elif colors[i-2] == 'B' and colors[i-1] == 'B' and colors[i] == 'B':
                bob_count += 1
        return alice_count > bob_count #if alice > bob, alice wins, else bob and if "AA", then both 0,hence Alice cannot make her turn hence Bob wins
                