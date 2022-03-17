class Solution {
    public void setZeroes(int[][] matrix) {
        // int R = matrix.length, C = matrix[0].length;
        // Set<Integer> rows = new HashSet<Integer>();
        // Set<Integer> cols = new HashSet<Integer>();
        // for(int i = 0; i < R; i++){
        //     for(int j = 0; j < C; j++){
        //         if(matrix[i][j] == 0){
        //             rows.add(i);
        //             cols.add(j);
        //         }
        //     }
        // }
        // for(int i = 0; i < R; i++){
        //     for(int j = 0; j < C; j++){
        //         if(rows.contains(i) || cols.contains(j)){
        //             matrix[i][j] = 0;
        //         }
        //     }
        // }
        int R = matrix.length, C = matrix[0].length;
        Boolean firstCol = false, firstRow = false;
        for(int i = 0; i < R; i++){
            if(matrix[i][0] == 0){
                firstCol = true;
                break;
            }
        }
        for(int j = 0; j < C; j++){
            if(matrix[0][j] == 0){
                firstRow = true;
                break;
            }
        }
        for(int i = 1; i < R; i++){
            for(int j = 1; j < C; j++){
                if(matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for(int i = 1; i < R; i++){
            for(int j = 1; j < C; j++){
                if(matrix[i][0] == 0 || matrix[0][j] == 0){
                    matrix[i][j] = 0;
                }
            }
        }
        if(firstRow){
           for(int j = 0; j < C; j++){
                matrix[0][j] = 0;
            }
        }
        if(firstCol){
           for(int i = 0; i < R; i++){
                matrix[i][0] = 0;
            } 
        }
        
    }
}