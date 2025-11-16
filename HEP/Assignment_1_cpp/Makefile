all:test_fourvector
clean:
	rm fourvector.o
	rm libfourvector.so
	rm test_fourvector.exe
fourvector.o: fourvector.cpp
	gcc -c -fPIC fourvector.cpp -o fourvector.o
libfourvector.so: fourvector.o
	gcc -shared -fPIC -o libfourvector.so fourvector.o
test_fourvector: libfourvector.so
	g++ test_fourvector.cpp -L ./ -lfourvector -o test_fourvector.exe
