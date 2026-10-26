# 공지·문의·알림으로 이어지는 고객 지원

[전체 기능](../README.md) · [매장과 예약](stores-and-reservations.md) · [지식 개선과 문의 추이](knowledge-improvement.md)

고객은 지역 공지와 장애 안내를 확인하고, 필요한 문의를 남기고, 예약·납부·이용 알림을 확인합니다. 관리자는 공지 노출과 문의 처리 상태를 관리합니다.

## 안내를 확인하고 문의를 처리합니다

| 사용자 행동 | FE가 하는 일 | BE가 하는 일 | 결과 |
|---|---|---|---|
| 공지 배너 확인 | 현재 노출할 배너를 받아 표시 | 노출 기간·지역 조건에 맞는 공지 조회 | 전체 또는 해당 지역 안내 |
| 이전 공지 보기 | 유형·지역 조건으로 목록과 상세 요청 | 삭제되지 않은 공지 이력 조회 | 종료된 안내도 다시 확인 |
| 일대일 문의 | 제목·내용 입력, 본인 문의 목록과 답변 표시 | 본인 문의 저장·조회, 상태에 맞는 수정·삭제 확인 | 문의와 처리 상태 |
| 관리자 답변 | 문의를 선택해 답변 저장 요청 | 현재 상태를 확인하고 답변·처리 결과 저장 | 고객이 조회할 답변 |
| 알림 확인 | 목록·미확인 수 표시, 읽음 요청 | 본인 알림 조회·읽음 상태 저장 | 같은 계정에서 관리하는 알림 상태 |

## 예약·이용 시점을 놓치지 않도록 돕습니다

예약 확정·취소·방문 전 안내, 납부 예정·연체, 로밍 시작·종료, 약정·할부 만료, 사용량 기준 도달 등 고객이 확인할 시점을 알림으로 제공합니다. 같은 이벤트의 알림을 반복 생성하지 않도록 서버에서 구분합니다.

알림 목록과 미확인 수는 서버 자료를 사용합니다. 목록을 불러오지 못한 상태를 새 알림이 없는 상태로 단정하지 않습니다. 읽음 처리를 요청하면 해당 계정의 상태를 갱신합니다.

지역별 문의 급증은 관리자가 상황을 살펴보는 자료입니다. 관리자가 실제 상황을 확인하고 공지를 작성하며, 감지 결과만으로 장애 배너를 자동 게시하지 않습니다.

## 수정·응답이 겹칠 때

문의 수정·삭제와 관리자 답변은 문의 상태를 확인한 뒤 처리합니다. 이미 답변한 문의를 고객 화면의 오래된 상태만 보고 수정하지 않습니다. 공지를 삭제하면 현재 목록·배너에서 제외하며, 종료 시각이 지난 공지는 배너와 이력 조회에서 다르게 다룹니다.

## 상세 구현과 검증

- Backend: [공지 노출·문의 상태·알림 규칙](https://github.com/ureca-UBot/UBot-BE/blob/98ba921c0e8271a8aa068a5bda56e85fe50c1ce7/docs/features/customer-support.md)
- Frontend: [공지 화면](https://github.com/ureca-UBot/UBot-FE/blob/develop/src/user/pages/NoticePage.tsx) · [문의 화면 연동](https://github.com/ureca-UBot/UBot-FE/blob/develop/src/user/inquiry/hooks/useMyInquiries.ts) · [알림 조회와 읽음 처리](https://github.com/ureca-UBot/UBot-FE/blob/develop/src/user/notification/hooks/useMyNotifications.ts)
- 관리자: [문의 처리 화면](https://github.com/ureca-UBot/UBot-FE/blob/develop/src/admin/pages/inquiry/InquiryListPage.tsx) · [공지 관리 화면](https://github.com/ureca-UBot/UBot-FE/blob/develop/src/admin/pages/notice/NoticeListPage.tsx)
