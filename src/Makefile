CXX=g++
CPATH = -I../3rd-party -I.
CFLAGS=-std=c++20 -w $(CPATH)

COMPILE_TEMPLATE=-o dir/main.exec dir/main.cpp

FIND=find
FFLAGS=-name

EXECUTABLE=*.exec
EXEC_FILES=$(shell $(FIND) $(FFLAGS) $(EXECUTABLE))

define compile
$(CXX) $(CFLAGS) $(subst dir,$(1),$(COMPILE_TEMPLATE))
endef

mcompiler : compiler
	$(call compile,compiler)

.PHONY : clean
clean :
	@for exec in $(EXEC_FILES); do \
		rm $$exec; \
	done
