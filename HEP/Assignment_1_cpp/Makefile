all:app
clean:
	rm hello.o
	rm libhello.so
	rm app
hello.o: hello.cpp
	gcc -c -fPIC hello.cpp -o hello.o
libhello.so: hello.o
	gcc -shared -fPIC -o libhello.so hello.o
app: libhello.so
	g++ app.cpp -L ./ -lhello -o app.exe
