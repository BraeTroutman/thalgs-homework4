{-
 - Generate all binary strings of length n
 -}

import Data.List (unfoldr, isInfixOf)
import Data.Functor
import System.Environment (getArgs)

allstrings = (unfoldr (\b -> let b' = (map (:) "01") <*> b in Just (b',b')) [""] !!) . pred

main = do
    n <- read.head <$> getArgs :: IO Int
    let strings = allstrings n
    let chosen = filter (isInfixOf "111") strings
    print strings
    print $ length strings
    print chosen
    print $ length chosen

