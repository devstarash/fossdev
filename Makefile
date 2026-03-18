.PHONY: create-practice remove-practice
create-practice:
ifndef NAME
	$(error NAME is not defiend)
	
endif
	mkdir -p $(NAME)

remove-practice:
ifndef NAME
	$(error NAME is not defiend)


endif
	rm -rf $(NAME)
