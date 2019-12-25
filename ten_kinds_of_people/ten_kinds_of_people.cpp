/*
Christian Felt
December 2019
Solves the 10 Kinds of People Problem on Kattis.
Solution strategy: Fill adjacent locations that have the same character with the fill character, 
similarly to in a paint program, starting from the initial point and see if fill character
reaches the destination point.
*/

#include <iostream>
#include <string>

using namespace std;

void fill_helper(int r0, int c0, int** board, int rows, int cols, char filler, char filled){
	if (board[r0][c0] == filled){
		board[r0][c0] = filler;
		if (r0 + 1 < rows){
			fill_helper(r0 + 1, c0, board, rows, cols, filler, filled);
		}
		if (r0 - 1 > -1){
			fill_helper(r0 - 1, c0, board, rows, cols, filler, filled);
		}
		if (c0 + 1 < cols){
			fill_helper(r0, c0 + 1, board, rows, cols, filler, filled);
		}
		if (c0 - 1 > -1){
			fill_helper(r0, c0 - 1, board, rows, cols, filler, filled);
		}
	}
	else{
		return;
	}	
}

void fill(int r0, int c0, int** board, int rows, int cols, char filler){
	char filled = board[r0][c0];
	fill_helper(r0, c0, board, rows, cols, filler, filled);
}

void print_board(int** board, int rows, int cols){
	for (int i = 0; i < rows; i++){
		for(int j = 0; j < cols; j++){
			cout << board[i][j];
		}
		cout << "\n";
	}
}

string query_board(int r1, int c1, int r2, int c2, int** board, int rows, int cols){
	char start = board[r1][c1];
	string return_value = "neither";
	fill(r1, c1, board, rows, cols, 4);
	if (board[r1][c1] == board[r2][c2]){
		if (start == 0){
			return_value = "binary";
		}
		else{
			return_value = "decimal";
		}
	}
	fill(r1, c1, board, rows, cols, start); // Return board to original state.
	return return_value;
}


int main(int argc, char *argv[]) {
	int r;
	cin >> r;
	int c;
	cin >> c;
	int** board = new int*[r];  // This is our only use of dynamic memory
	// and it may as well last as long as the program, so no destructor needed.
	for(int i = 0; i < r; i++){
		board[i] = new int[c];
	}
	cin.ignore();  // Ingnore the newline character after the previous input.
	for(int i = 0; i < r; i++){
		string this_line;
		getline(cin, this_line);
		for (string::size_type j = 0; j < this_line.size(); j++){
			int this_entry = (int)(this_line[j]) - 48;
			board[i][j] = this_entry;
		}
	}
	int n;
	cin >> n;
	for (int i = 0; i < n; i++){
		int r1;
		int c1;
		int r2;
		int c2;
		cin >> r1;
		cin >> c1;
		cin >> r2;
		cin >> c2;
		cout << query_board(r1 - 1, c1 - 1, r2 - 1, c2 - 1, board, r, c) << "\n";		
	}
}