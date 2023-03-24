targets=bin/generate_strings bin/tabular bin/monoidic

.phony: all clean
all: $(targets)

objdir="-odir objects"
intdir="-hidir interface"

bin/%: src/%.hs
	ghc -o $@ $(objdir) $(intdir) $^

clean: 
	-rm $(targets)

