import pandas as pd
import numpy as np
import random

# 1. サンプル用の選択肢を定義
food_options = ['ラーメン', 'カレー', '寿司', 'パスタ', 'ハンバーグ', 'サラダ']
device_options = ['iPhone', 'Android', 'PC', 'Tablet']

def generate_survey_data(n=10):
    data = []
    for i in range(n):
        # 複数回答（1〜3個をランダムに選択）
        fav_foods = random.sample(food_options, k=random.randint(1, 3))
        # 複数回答（デバイス）
        devices = random.sample(device_options, k=random.randint(1, 2))
        
        row = {
            'ユーザーID': f'U{i+1:03}',
            '年齢': random.randint(20, 60),
            '満足度': random.choice([1, 2, 3, 4, 5, None]), # 欠損値を混ぜる
            '好きな食べ物': fav_foods, # リスト形式
            # '利用デバイス': devices     # リスト形式
        }
        data.append(row)
    
    return pd.DataFrame(data)

def generate_duplicate_example():
    # 1. ユーザーマスター (本来は1人1行のはずが、住所変更などで重複しているケース)
    df_user = pd.DataFrame({
        'user_id': [1, 2, 2, 3],  # ID 2番が重複している
        'user_name': ['田中', '佐藤_旧', '佐藤_新', '鈴木']
    })

    # 2. 購入履歴 (1人のユーザーが複数回購入している)
    df_order = pd.DataFrame({
        'user_id': [1, 2, 2, 4],
        'item': ['リンゴ', 'バナナ', 'メロン', 'ブドウ'],
        'price': [100, 200, 300, 400]
    })
    
    return df_user, df_order

# # データ生成
# df = generate_survey_data(5)

# # 2. convert_dtypesを適用してみる
# # リストが入っている列は「object」のまま維持され、数値列などは適切な型に整理されます
# df_optimized = df.convert_dtypes()

# print("--- 生成されたデータフレーム ---")
# print(df_optimized)
# print("\n--- 各列のデータ型 ---")
# print(df_optimized.dtypes)