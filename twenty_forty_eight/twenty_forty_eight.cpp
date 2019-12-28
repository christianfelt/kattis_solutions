/*
Christian Felt
December 2019
Solves the 2048 problem on Kattis.
*/

#include <iostream>
#include <vector>
using namespace std;


class Tile
{
	/* Represent a tile. */
	public:
		bool merged; // Whether or not a tile has been merged with another tile this turn.
		int number; // The number value on the tile.
		
		Tile()
		{
			number = 0;
			merged = false;
		}
		
		Tile(int number, bool merged)
		{
			number = number;
			merged = merged;
		}
};

void display_board(vector<vector<Tile> >& board)
/* Print numbers on tiles and their arrangement on the board. */
{
	for (int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			cout << board[i][j].number << " ";
		}
		cout << "\n";
	}
}

void reset_merged_markers(vector<vector<Tile> >& board)
/* Set all merged instance variables to false. */
{
	for (int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			board[i][j].merged = false;
		}
	}
}

void do_move(int move, vector<vector<Tile> >& board)
/* Do a single move of the game. */
{
	reset_merged_markers(board);
	if (move == 0) // Left.
	{
		bool did_swap = true;
		while(did_swap)
		{
			did_swap = false;
			for (int i = 0; i < 4; i++)
			{
				for(int j = 0; j < 4; j++)
				{
					if (j == 0)
					{
						
					}
					else if (board[i][j-1].number == 0 && board[i][j].number != 0)
					{
						board[i][j-1] = board[i][j];
						board[i][j].number = 0;
						board[i][j].merged = false;
						did_swap = true;
					}
					else if ((board[i][j-1].number == board[i][j].number) && (board[i][j-1].merged == false && board[i][j].merged == false))
					{
						board[i][j-1].number = 2 * board[i][j-1].number;
						board[i][j-1].merged = true;
						board[i][j].number = 0;
						board[i][j].merged = false;
						did_swap = true;
					}
				}
			}
		}
	}
	else if (move == 1)  // Up
	{
		bool did_swap = true;
		while(did_swap)
		{
			did_swap = false;
			for (int j = 0; j < 4; j++)
			{
				for(int i = 0; i < 4; i++)
				{
					if (i == 0)
					{
						
					}
					else if (board[i-1][j].number == 0 && board[i][j].number != 0)
					{
						board[i-1][j] = board[i][j];
						board[i][j].number = 0;
						board[i][j].merged = false;
						did_swap = true;
					}
					else if ((board[i-1][j].number == board[i][j].number) && (board[i-1][j].merged == false && board[i][j].merged == false))
					{
						board[i-1][j].number = 2 * board[i-1][j].number;
						board[i-1][j].merged = true;
						board[i][j].number = 0;
						board[i][j].merged = false;
						did_swap = true;
					}
				}
			}
		}
	}
	else if (move == 2)  // Right
	{
		bool did_swap = true;
		while(did_swap)
		{
			did_swap = false;
			for (int i = 0; i < 4; i++)
			{
				for(int j = 3; j > -1; j--)
				{
					if (j == 3)
					{
						
					}
					else if (board[i][j+1].number == 0 && board[i][j].number != 0)
					{
						board[i][j+1] = board[i][j];
						board[i][j].number = 0;
						board[i][j].merged = false;
						did_swap = true;
					}
					else if ((board[i][j+1].number == board[i][j].number) && (board[i][j+1].merged == false && board[i][j].merged == false))
					{
						board[i][j+1].number = 2 * board[i][j+1].number;
						board[i][j+1].merged = true;
						board[i][j].number = 0;
						board[i][j].merged = false;
						did_swap = true;
					}
				}
			}
		}
	}
	else if (move == 3)  // Down
	{
		bool did_swap = true;
		while(did_swap)
		{
			did_swap = false;
			for (int j = 0; j < 4; j++)
			{
				for(int i = 3; i > -1; i--)
				{
					if (i == 3)
					{
						
					}
					else if (board[i+1][j].number == 0 && board[i][j].number != 0)
					{
						board[i+1][j] = board[i][j];
						board[i][j].number = 0;
						board[i][j].merged = false;
						did_swap = true;
					}
					else if ((board[i+1][j].number == board[i][j].number) && (board[i+1][j].merged == false && board[i][j].merged == false))
					{
						board[i+1][j].number = 2 * board[i+1][j].number;
						board[i+1][j].merged = true;
						board[i][j].number = 0;
						board[i][j].merged = false;
						did_swap = true;
					}
				}
			}
		}
	}
}


int main(int argc, char *argv[]) {
	/* Solve the 2048 problem. */
	vector<vector<Tile> > board(4, vector<Tile>(4));
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			int this_number;
			cin >> this_number;
			board[i][j].number = this_number;
		}
	}
	int move;
	cin >> move;
	do_move(move, board);
	display_board(board);
}