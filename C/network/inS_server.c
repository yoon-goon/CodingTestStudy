#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>



#define PORTNUM 9000

int main(void) {
	char buf[256];
	struct sockaddr_in sin, cli;
	int sd, ns, clientlen = sizeof(cli);
	int cnt = 0;

	if ((sd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
		perror("socket");
		exit(1);
	}

	memset((char*)&sin, '\0', sizeof(sin));
	sin.sin_family = AF_INET;
	sin.sin_port = htons(PORTNUM);
	sin.sin_addr.s_addr = inet_addr("127.0.0.1");

	if (bind(sd, (struct sockaddr*)&sin, sizeof(sin))) {
		perror("bind");
		exit(1);	}	if (listen(sd, 5)) {
		perror("listen");
		exit(1);
	}

	printf("Waiting...\n");

	if ((ns = accept(sd, (struct sockaddr*)&cli, &clientlen)) == -1) {
		perror("accept");
		exit(1);
	}

	printf("[Client Connected]\n");

	while (1) {
		memset(buf, 0, sizeof(buf));
		if (read(ns, buf, sizeof(buf)) == -1) {
			perror("read");
			exit(1);
		}

		if (strcmp(buf, "c") == 0 || strcmp(buf, "C") == 0) {
			sprintf(buf, "%d", cnt); // 버퍼에 cnt 변환하여 클라이언트 전달
			printf("[Message cnt Response (cnt: %s) ]\n", buf);
		}
		else if (strcmp(buf, "q") == 0 || strcmp(buf, "Q") == 0) {
			printf("[Client Disconnected]\n");
			break;
		}
		else {
			cnt++;
			printf("Received Message: %s\n", buf);
		}

		if (write(ns, buf, strlen(buf) + 1) == -1) {
			perror("write");
			exit(1);
		}
	}

	close(ns);
	close(sd);

	return 0;

}