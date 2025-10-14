class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        def check_if_possible(index) -> bool:
            if index==0:
                return True if flowerbed[1]==0 and flowerbed[0]==0 else False
            
            if index==len(flowerbed)-1:
                return True if flowerbed[len(flowerbed)-2]==0 and flowerbed[len(flowerbed)-1]==0 else False

            return True if flowerbed[index]==0 and flowerbed[index-1]==0 and flowerbed[index+1]==0 else False

        if len(flowerbed)==1:
            if flowerbed[0]==0 and n==1 or n==0:
                return True
            return False
        
        for idx, place in enumerate(flowerbed):
            # if idx!=0 and idx!=len(flowerbed)-1:
            print(check_if_possible(idx))
            if check_if_possible(idx):
                flowerbed[idx]=1
                n-=1

        print(flowerbed, n)

        if n > 0:
            return False 
        
        return True
                
            