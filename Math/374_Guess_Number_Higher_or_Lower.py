/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *		      1 if num is lower than the picked number
 *                    otherwise return 0
 * int guess(int num);
 */
int guess(int num);
int guessNumber(int n){

    signed int low = 1, high = n, mid, result;
    while(low<=high)
    {
        mid = low + (high-low)/2;
        result=guess(mid);
        if(result==0)
        return mid;
        else if (result == 1)
            low = mid + 1;
        else
            high = mid - 1;
    }
return 0;	
}
