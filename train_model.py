# pip install pandas scikit-learn joblib

import pandas as pd
import re
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# 1. 데이터 로드 (사용자 경로 지정)
DATA_PATH = r"IMDB Dataset.csv"

def clean_text(text):
    """HTML 태그 제거 및 텍스트 정제"""
    text = str(text).lower() # 소문자 변환
    text = re.sub(r'<br\s*/?>', ' ', text) # <br> 태그 제거
    text = re.sub(r'[^a-zA-Z\s]', '', text) # 특수문자 제거 (영어만 남김)
    return text

print("🔄 Loading dataset...")
try:
    df = pd.read_csv(DATA_PATH)
    print(f"✅ Dataset loaded: {df.shape[0]} reviews found.")
except FileNotFoundError:
    print("❌ Error: 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
    exit()

# 2. 전처리 (Preprocessing)
print("🧹 Cleaning text data...")
df['review'] = df['review'].apply(clean_text)

# 3. 학습/테스트 데이터 분리
X = df['review']
y = df['sentiment'] # positive / negative

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. 파이프라인 구축 (TF-IDF 벡터화 + 로지스틱 회귀)
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000, stop_words='english')),
    ('clf', LogisticRegression(random_state=42))
])

# 5. 모델 학습
print("🚀 Training the model (this may take a moment)...")
pipeline.fit(X_train, y_train)

# 6. 성능 평가
print("📊 Evaluating model...")
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"🏆 Model Accuracy: {accuracy:.2f}")
print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred))

# 7. 모델 저장
# 이 파일을 저장해야 main.py에서 매번 학습하지 않고 바로 분석할 수 있습니다.
model_filename = 'sentinema_model.pkl'
joblib.dump(pipeline, model_filename)

print(f"💾 Model saved to '{model_filename}'")
