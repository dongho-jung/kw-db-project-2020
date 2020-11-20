# kw-db-project-2020
광운대 디비만만팀 데이터베이스및응용 프로젝트 

## Dummy Data Server 구축
1. apps/dummy_data 경로에서 `docker build -t kw_db .`. 최종 이미지 사이즈는 1.5GB
2. `docker run -d -p 5432:5432 --name kw_db kw_db`로 컨테이너 생성
3. 로컬호스트의 5432포트로 DB에 접근

### NOTE:
- 이미지를 처음 빌드시 필요한 base image 다운로드와 기타 초기화 작업으로 인해 시간이 다소 소요될 수 있음
- 최종 이미지 크기는 1.5GB
- main.py에서 각 *_rows 별로 itertools.islice 값을 조절하여 더미데이터 크기를 조절
- -p A:B는 호스트의 A포트를 컨테이너의 B포트에 바인딩. 만약 호스트가 기존에 5432포트를 사용중이라면 뒤의 포트번호를 변경
