import Data.Array ( array, Array(..), (!) )
import System.Environment ( getArgs )
import Data.List ( unfoldr )

main = do
    n <- read.head <$> getArgs :: IO Int
    print $ dpalt n

tupsum :: (Integer, Integer, Integer) -> Integer
tupsum (a,b,c) = a+b+c

-- dp n is the 3-tuple of the number of strings of length n with exactly 0, 1, and 2 consecutive 1's respectively
dp :: Int -> Array Int (Integer, Integer, Integer)
dp n = sltn
    where sltn = array (1,n) [(i, go i) | i <- [1..n]]
          go 1 = (1,1,0)
          go n = let (a,b,c) = sltn ! (n-1) in (a+b+c, a, b)

dpalt :: Int -> Integer
dpalt 0 = 0
dpalt 1 = 2
dpalt n = sltn
    where (sltn,_,_) = result (1,1,0) n
          result !r !0 = r
          result (!a,!b,!c) !n = result (a+b+c, a, b) (n-1)

