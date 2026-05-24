---
typora-root-url: ../
layout: single
title: >
  Docker daemon not running 오류 해결 방법
seo_title: >
  Docker daemon not running 해결
date: 2024-10-30T07:39:00+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: ko
translation_id: docker-daemon-not-running
header:
   teaser: /images/2026-05-23-docker-daemon-not-running/docker-daemon-not-running-hero.png
   overlay_image: /images/2026-05-23-docker-daemon-not-running/docker-daemon-not-running-hero.png
   overlay_filter: 0.35
   image_description: >
     Docker daemon not running 오류 해결 방법 주제를 한눈에 설명하는 시각 자료입니다.
excerpt: >
  Cannot connect to the Docker daemon 오류를 Docker Desktop 또는 Docker service 실행, socket 권한, Docker context, DOCKER_HOST 점검 순서로 해결합니다.
seo_description: >
  Cannot connect to the Docker daemon 오류를 Docker Desktop 또는 Docker service 실행, socket 권한, Docker context, DOCKER_HOST 점검 순서로 해결합니다.
categories:
  - ko_Troubleshooting
tags:
  - Docker
  - Containers
  - DevOps
  - Linux
  - Windows
---

## 핵심 요약

`Cannot connect to the Docker daemon`은 Docker client 명령은 실행됐지만 Docker engine과 통신하지 못했다는 뜻입니다.
Docker Desktop 또는 Docker service를 실행하고, engine 상태, socket 권한, Docker context, `DOCKER_HOST`를 확인한 뒤 `docker version` 또는 `docker info`로 검증합니다.

![Docker daemon 미실행 상태에서 service start, socket check, container status 성공 경로를 보여주는 이미지](/images/2026-05-23-docker-daemon-not-running/docker-daemon-not-running-hero.png)

이미지는 client와 engine의 관계를 보여줍니다.
`docker` 명령은 client입니다.
container를 실행하려면 background에서 daemon 또는 engine이 동작해야 합니다.

## 대표 오류 메시지

아래 메시지를 볼 수 있습니다.

```text
Cannot connect to the Docker daemon at unix:///var/run/docker.sock.
Is the docker daemon running?
```

Windows나 Docker Desktop에서는 표현이 조금 다를 수 있습니다.
핵심은 CLI가 engine에 연결하지 못한다는 점입니다.

먼저 확인합니다.

```bash
docker version
```

client 정보는 나오는데 server 정보가 실패하면 CLI는 설치되어 있지만 daemon이 준비되지 않은 상태입니다.

## 1. Windows 또는 macOS에서는 Docker Desktop 실행

Docker Desktop을 사용한다면 application이 실제로 실행 중인지 확인해야 합니다.
terminal을 여는 것만으로는 충분하지 않습니다.

순서는 다음과 같습니다.

1. Docker Desktop을 실행합니다.
2. engine status가 running이 될 때까지 기다립니다.
3. 새 terminal을 엽니다.
4. 아래 명령을 실행합니다.

```bash
docker version
docker info
```

Docker Desktop이 starting 상태에서 멈춘다면 troubleshoot menu를 사용하거나 app을 재시작합니다.
Windows에서는 virtualization 또는 WSL integration 설정도 확인해야 합니다.

## 2. Linux에서는 Docker Service 실행

많은 Linux 환경에서는 daemon이 `systemd`로 관리됩니다.

상태 확인:

```bash
sudo systemctl status docker
```

시작:

```bash
sudo systemctl start docker
```

부팅 시 자동 실행:

```bash
sudo systemctl enable docker
```

그 다음 검증합니다.

```bash
docker info
```

service가 시작되지 않으면 log를 확인합니다.

```bash
sudo journalctl -u docker --no-pager -n 100
```

log에는 잘못된 daemon configuration, storage driver 문제, dependency 누락, port conflict 같은 원인이 나올 수 있습니다.

## 3. Linux Socket 권한 확인

`sudo`를 붙이면 되고, 그냥 실행하면 실패한다면 daemon은 실행 중이지만 현재 user가 Docker socket에 접근하지 못하는 것입니다.

테스트:

```bash
sudo docker info
docker info
```

`sudo`만 성공한다면 보안 정책에 맞는 경우에만 user를 Docker group에 추가합니다.

```bash
sudo usermod -aG docker $USER
```

그 다음 로그아웃 후 다시 로그인합니다.
새 terminal만 여는 것으로는 부족할 수 있습니다.
group membership은 보통 login 시점에 적용됩니다.

보안 참고: Docker group 권한은 강력합니다.
신뢰할 수 있는 user에게만 부여해야 합니다.

## 4. Docker Context 확인

Docker는 여러 context를 사용할 수 있습니다.
현재 context가 remote engine이나 unavailable engine을 가리키면 local 명령도 실패할 수 있습니다.

context 목록:

```bash
docker context ls
```

기본 local context 사용:

```bash
docker context use default
```

다시 확인합니다.

```bash
docker ps
```

최근 remote Docker host, cloud context, development container setup을 사용했다면 특히 확인할 가치가 있습니다.

## 5. DOCKER_HOST 환경 변수 확인

`DOCKER_HOST` 환경 변수는 Docker client가 연결할 위치를 바꿀 수 있습니다.

Bash:

```bash
echo $DOCKER_HOST
```

PowerShell:

```powershell
echo $env:DOCKER_HOST
```

오래되었거나 사용할 수 없는 daemon을 가리킨다면 현재 shell에서 제거하고 다시 시도합니다.

PowerShell:

```powershell
Remove-Item Env:DOCKER_HOST
```

Bash:

```bash
unset DOCKER_HOST
```

## 6. 작은 Container로 검증

daemon이 실행된 뒤 아래 명령으로 테스트합니다.

```bash
docker run hello-world
```

image pull이 되고 test container가 정상 종료되면 client와 daemon 통신이 되는 것입니다.

기존 프로젝트라면 그 다음 확인합니다.

```bash
docker compose version
docker compose up
```

Docker는 되는데 Compose만 실패한다면 daemon 문제가 아닐 수 있습니다.
Compose file, image build, port mapping, environment variable을 봐야 합니다.

## 흔한 실수

첫 번째 실수는 engine이 단순히 꺼져 있는지 확인하기 전에 Docker를 재설치하는 것입니다.
먼저 service를 시작하세요.

두 번째 실수는 client와 server 차이를 무시하는 것입니다.
`docker --version`은 CLI 존재만 증명합니다.
daemon 실행 여부를 증명하지 않습니다.

세 번째 실수는 permission 문제를 이해하지 않고 계속 `sudo`만 붙이는 것입니다.
동작은 할 수 있지만 user/socket 문제를 숨깁니다.

네 번째 실수는 Docker context나 `DOCKER_HOST`를 잊는 것입니다.
client가 local machine이 아닌 다른 곳에 연결하려고 할 수 있습니다.

## 함께 보면 좋은 글

- [GitHub Actions Build Failed 해결](/ko_troubleshooting/github-actions-build-failed/)
- [GitHub Pages Jekyll build 실패 해결](/ko_troubleshooting/github-pages-jekyll-build-failed/)
- [Docker: Start the daemon](https://docs.docker.com/engine/daemon/start/)
- [Docker: Linux post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/)

## 최종 체크리스트

```text
[ ] Docker Desktop 또는 Docker service가 실행 중이다.
[ ] `docker version`에 client와 server가 모두 나온다.
[ ] Linux user가 Docker socket에 접근할 권한이 있다.
[ ] Docker context가 기대한 engine을 가리킨다.
[ ] `DOCKER_HOST`가 오래된 daemon을 가리키지 않는다.
[ ] `docker run hello-world`가 성공한다.
```

먼저 daemon 연결을 고쳐야 합니다.
Dockerfile, Compose file, port mapping은 client가 engine과 통신한 뒤에 디버깅하는 것이 순서입니다.

## 자주 묻는 질문

### 이 글은 언제 먼저 적용하면 좋나요?

오류 메시지, 실행한 명령, 사용 중인 OS와 버전을 먼저 기록한 뒤 이 글의 원인별 순서대로 확인하는 것이 좋습니다.

### 초보자가 가장 먼저 확인할 부분은 무엇인가요?

처음에는 환경 변수, 설치 경로, 권한, 캐시처럼 재현 가능성이 높은 항목부터 확인하세요. 그다음 로그와 설정 파일을 비교하면 원인을 좁히기 쉽습니다.

### 더 찾아볼 때 어떤 키워드를 쓰면 좋나요?

추가 검색할 때는 "Docker daemon not running 오류 해결 방법" 같은 핵심 문구와 error message, version, Windows, GitHub Pages, Jekyll 같은 실제 환경 키워드를 붙이면 더 정확한 결과를 얻기 쉽습니다.
