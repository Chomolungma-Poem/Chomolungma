COMMAND=g++ -std=c++14 -w
COMPILE_TEMPLATE=-o dir/main dir/* -I../3rd-party

define compile
$(COMMAND) $(subst dir,$(1),$(COMPILE_TEMPLATE))
endef

COMPILER = compiler

$(COMPILER) : $(COMPILER)/*
	$(call compile,$(COMPILER))
