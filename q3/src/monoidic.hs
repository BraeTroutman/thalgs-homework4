{-
 - compute the number of bitstrings on length n
 - that don't contain the substring 111
 -}

import System.Environment
import qualified Data.Semigroup as Semigroup

main :: IO ()
main = do
    n <- read.head <$> getArgs :: IO Integer
    print $ x00 $ dp (n+1)

-- Semigroup.mtimesDefault uses the repeated squaring property
-- of all semigroups (in our case our semigroup is 3x3 matrices
-- under the function of multiplication) to apply a monoidic
-- operation to a function n times in O(log n) time
dp n = Semigroup.mtimesDefault n mat
    where mat = Matrix 1 1 1 1 0 0 0 1 0

-- our 3x3 matrix datatype
data Matrix3x3 = Matrix {
    x00 :: Integer, x01 :: Integer, x02 :: Integer,
    x10 :: Integer, x11 :: Integer, x12 :: Integer,
    x20 :: Integer, x21 :: Integer, x22 :: Integer
    } deriving Show

-- make matrix an instance of Semigroup by defining (<>) as matmul
instance Semigroup Matrix3x3 where
    (Matrix a00 a01 a02 a10 a11 a12 a20 a21 a22) <> (Matrix b00 b01 b02 b10 b11 b12 b20 b21 b22) = 
        Matrix {
                x00 = a00*b00 + a01*b10 + a02*b20,
                x01 = a00*b01 + a01*b11 + a02*b21,
                x02 = a00*b02 + a01*b12 + a02*b22,
                x10 = a10*b00 + a11*b10 + a12*b20,
                x11 = a10*b01 + a11*b11 + a12*b21,
                x12 = a10*b02 + a11*b12 + a12*b22,
                x20 = a20*b00 + a21*b10 + a22*b20,
                x21 = a20*b01 + a21*b11 + a22*b21,
                x22 = a20*b02 + a21*b12 + a22*b22
        }

-- make matrix an instance of Monoid by specifying an identity element,
-- in this case the 3x3 Identity matrix
instance Monoid Matrix3x3 where
    mempty = Matrix 1 0 0 0 1 0 0 0 1

