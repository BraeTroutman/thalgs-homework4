import Data.Array ( array, Array(..), (!) )
import System.Environment ( getArgs )
import Data.List ( unfoldr )

main = do
    n <- read.head <$> getArgs :: IO Int
    let result = dp n ! n
    putStrLn $ show (length result) ++ " valid strings of length " ++ show n
    mapM_ putStrLn result

-- dp n is the 3-tuple of the number of strings of length n with exactly 0, 1, and 2 consecutive 1's respectively
dp :: Int -> Array Int [String]
dp n = sltn
    where sltn = array (0,n) [(i, go i) | i <- [0..n]]
          go 0 = [""]
          go 1 = ["0", "1"]
          go 2 = ["00", "01", "10", "11"]
          go n = (map ("110"++) (sltn ! (n-3))) ++
                 (map ("10"++)  (sltn ! (n-2))) ++
                 (map ("0"++)   (sltn ! (n-1)))

dpalt :: Int -> Integer
dpalt 0 = 0
dpalt 1 = 2
dpalt n = sltn
    where (sltn,_,_) = result (1,1,0) n
          result !r !0 = r
          result (!a,!b,!c) !n = result (a+b+c, a, b) (n-1)

