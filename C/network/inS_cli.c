#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORTNUM 9000

int main(void) {
	int sd;
	char buf[256];
	struct sockaddr_in sin;

	if ((sd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
		perror("socket");
		exit(1);
	}

	memset((char*)&sin, '\0', sizeof(sin));
	sin.sin_family = AF_INET;
	sin.sin_port = htons(PORTNUM);
	sin.sin_addr.s_addr = inet_addr("127.0.0.1");

	if (connect(sd, (struct sockaddr*)&sin, sizeof(sin))) {
		perror("connect");
		exit(1);
	}

	while (1) {
		printf("Input message: ");
		fgets(buf, sizeof(buf), stdin);
		buf[strcspn(buf, "\n")] = 0; // 개행문자 삭제

		if (write(sd, buf, strlen(buf) + 1) == -1) {
			perror("write");
			exit(1);
		}

		if (strcmp(buf, "q") == 0 || strcmp(buf, "Q") == 0) {
			printf("[Disconnection Request]\n");
			break;
		}
		else if (strcmp(buf, "c") == 0 || strcmp(buf, "C") == 0) {
			printf("[Message Cnt Request]\n");

			memset(buf, 0, sizeof(buf)); // 버퍼 초기화
			if (read(sd, buf, sizeof(buf)) == -1) { // 서버로부터 데이터를 읽어들여 버퍼 buf에 저장
				perror("read");
				exit(1);
			}

			printf("[Text From Server: %s ]\n", buf);
		}
		else {
			// 서버 응답 대기
			memset(buf, 0, sizeof(buf));
			if (read(sd, buf, sizeof(buf)) == -1) {
				perror("read");
				exit(1);
			}

			printf("[Text From Server: %s ]\n", buf);
		}
	}
	close(sd);

	return 0;
}