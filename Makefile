PREFIX = $(NDK)/toolchains/llvm/prebuilt/linux-x86_64
TARGET = aarch64-linux-android
ANDROID_API ?= 21

CFLAGS = -O0 -Wall -Wextra -pedantic -Wformat -Werror=format-security
PROGRAM = getroot
CC = $(PREFIX)/bin/$(TARGET)$(ANDROID_API)-clang
STRIP = $(PREFIX)/bin/$(TARGET)-strip

hello: hello.c
	$(CC) -o $@ $^ $(CFLAGS)

all: hello
