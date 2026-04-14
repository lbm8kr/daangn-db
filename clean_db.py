import pandas as pd

# 1. 깃허브에 있는 CSV 파일 읽기
file_path = "daangn_with_coords.csv"
try:
    df = pd.read_csv(file_path)
    print(f"원본 데이터 불러오기 완료. (총 {len(df)}줄)")
except Exception as e:
    print(f"파일을 찾을 수 없습니다: {e}")
    exit()

# 2. 중복된 주소 제거 (full_name 기준, 마지막에 추가된 것만 남김)
df_clean = df.drop_duplicates(subset=['full_name'], keep='last')
removed_count = len(df) - len(df_clean)
print(f"중복 데이터 {removed_count}개 제거 완료.")

# 3. 없는 번호(region_id가 비어있는 곳) 체크
missing_ids = df_clean[df_clean['region_id'].isna()]
if not missing_ids.empty:
    print(f"\n⚠️ 아이디가 누락된 주소가 {len(missing_ids)}개 있습니다:")
    for index, row in missing_ids.iterrows():
        print(f"- {row['full_name']}")
else:
    print("\n✅ 누락된 아이디가 없습니다.")

# 4. 정리된 데이터를 다시 동일한 이름으로 덮어쓰기 저장
df_clean.to_csv(file_path, index=False, encoding="utf-8-sig")
print("\n파일 저장 완료!")
