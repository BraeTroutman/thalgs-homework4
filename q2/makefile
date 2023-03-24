targets=bin/shortestPath bin/longestPath

.phony: all clean
all: $(targets)

clean:
	-rm $(targets)

bin/%: src/%.hs
	ghc -odir build -hidir build -o $@ $^

