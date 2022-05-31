
- front-end
  - tokenizer
  - parser
  - code generator
- back-end
  - virtual machine
  - B-tree
  - pager
  - os interface

## P01

- **REPL** (read-execute-print loop)
  - 读取﹣求值﹣输出循环 / **交互式顶层构件**
  - 一个编程环境. 因它能立刻对初学者做出回应. 对学习一门语言具有很大的帮助.
  - via: [wikipedia](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop).
- ✖ B Tree
  - via: [Youtube-29:45](https://www.youtube.com/watch?v=aZjYr87r1b8).
- `size_t` & `ssize_t`
  - `size_t `
    - 32 Bit: `typedef unsigned int size_t;`.
    - 64 Bit: `typedef unsigned long size_t;`.
    - 注意写函数的时候, 无符号数不要和符号数比较.
      ```c
      #include <stdio.h>
      #include <string.h>
      int main(){
          int i = -1;
          if(i > strlen("Demon")) printf("Hello World");
          else printf("Hello Demon");
          return 0;
      } //Hello World via http://demon.tw/programming/c-size_t-pitfall.html
      ```
  - `ssize_t `
    - 32 Bit: `int`.
    - 64 Bit: `long int`.
    - via: https://blog.csdn.net/bzhxuexi/article/details/19899803 & https://stackoverflow.com/questions/2550774/what-is-size-t-in-c
- getline in C.
  - ```c
    // from https://c-for-dummies.com/blog/?p=1112
    #include <stdio.h>
    
    int input(char *s,int length);
    
    int main(){
        char *buffer;
        size_t bufsize = 32;
        size_t characters;
    
        buffer = (char *)malloc(bufsize * sizeof(char));
        if( buffer == NULL){
            perror("Unable to allocate buffer");
            exit(1);
        }
    
        printf("Type something: ");
        characters = getline(&buffer,&bufsize,stdin);
        printf("%zu characters were read.\n",characters);
        printf("You typed: '%s'\n",buffer);
    
        return(0);
    }
    // case two
    #include <stdio.h>
    
    int input(char *s,int length);
    
    int main()
    {    
        char *b;
        size_t bufsize = 0;
        size_t characters;
    
        printf("Type something: ");
        characters = getline(&b, &bufsize, stdin);
        printf("%ld\n", bufsize);
        printf("%zu characters were read.\n", characters);
        printf("You typed: '%s'\n", b);
    
        return(0);
    }
    ```
    - 会发现在 `char` 指针做缓冲区的时候, `bufsize` 默认为 `120`, 就算读入缓冲超过 `120` , 也会加倍为`240`. 但是, char 指针可以

      ```
      > ./test
      Type something: dsdsa
      120
      6 characters were read.
      You typed: '����'
      
      > ./test
      Type something: testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttestt
      240
      130 characters were read.
      You typed: 'testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttestt
      '
      ```
    - more via: https://stackoverflow.com/questions/20036074/length-of-line-in-getline-function-c.

## P02

- `.exit`: "meta-commands"


## P03