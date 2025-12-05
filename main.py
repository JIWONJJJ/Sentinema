import os
import argparse
import joblib
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# ==========================================
# 1. 설정 및 데모 데이터 (The "Fuel")
# ==========================================

# 모델 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'sentinema_model.pkl')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')

# 데모용 영화 데이터 (제목: [리뷰 리스트])
# 학습 데이터(IMDb)에는 제목이 없으므로, 시연을 위해 직접 수집한 소량의 데이터입니다.
DEMO_DATA = {
    "inception": [
        "The dream sequences were mind-blowing and visually stunning.",
        "A masterpiece of sci-fi cinema, Nolan is a genius.",
        "Too complicated, I got lost in the plot layers.",
        "Hans Zimmer's score is legendary and adds so much tension.",
        "The ending left me confused but in a good way.",
        "Brilliant acting by DiCaprio, but the story is a bit heavy.",
        "One of the best movies I have ever seen. Original and gripping."
    ],
    "parasite": [
        "A sharp social commentary wrapped in a thriller.",
        "The basement scene gave me chills. Bong Joon-ho is a master.",
        "Funny at first, but it gets dark very quickly.",
        "Absolute masterpiece. The cinematography is perfect.",
        "It shows the gap between the rich and poor so effectively.",
        "A bit too disturbing for my taste, but well made."
    ],
    "joker": [
        "Joaquin Phoenix deserves an Oscar for this performance.",
        "Dark, depressing, but an incredible character study.",
        "It was hard to watch because it felt so real.",
        "Beautifully shot, but the message is controversial.",
        "A psychological masterpiece. Not your typical comic book movie."
    ]
}

# ==========================================
# 2. 핵심 기능 함수 (The Logic)
# ==========================================

def load_model():
    """저장된 AI 모델(.pkl)을 불러옵니다."""
    if not os.path.exists(MODEL_PATH):
        print(f"❌ Error: Model file not found at {MODEL_PATH}")
        print("💡 Tip: Run 'train_model.py' first to generate the model.")
        return None
    print(f"🔄 Loading AI Model from '{MODEL_PATH}'...")
    return joblib.load(MODEL_PATH)

def generate_wordcloud(text_data, movie_name):
    """리뷰 텍스트에서 워드클라우드를 생성하고 이미지로 저장합니다."""
    # 모든 리뷰를 하나의 긴 문장으로 합침
    combined_text = " ".join(text_data)
    
    # 워드클라우드 생성
    wc = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(combined_text)
    
    # 출력 폴더 확인 및 생성
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    # 이미지 파일 저장
    save_path = os.path.join(OUTPUT_DIR, f"{movie_name}_wordcloud.png")
    wc.to_file(save_path)
    print(f"🎨 WordCloud saved to: {save_path}")

def analyze_movie(movie_name):
    """특정 영화의 리뷰를 분석하고 결과를 출력합니다."""
    key = movie_name.lower()
    
    # 1. 데모 데이터 확인
    if key not in DEMO_DATA:
        print(f"\n⚠️  Sorry, '{movie_name}' is not in our demo database.")
        print(f"   Available movies: {', '.join(DEMO_DATA.keys())}")
        print("💡 Want to add this movie? Please contribute to our repository via Pull Request!")
        return

    reviews = DEMO_DATA[key]
    print(f"\n🎬 Analyzing reviews for: **{movie_name.capitalize()}**")
    print(f"   Found {len(reviews)} sample reviews.")

    # 2. 모델 로드
    model = load_model()
    if model is None:
        return

    # 3. 감정 예측 (Sentiment Prediction)
    print("🧠 AI Interpreting emotions...")
    predictions = model.predict(reviews)
    
    # 결과 집계
    pos_count = list(predictions).count('positive')
    neg_count = list(predictions).count('negative')
    total = len(reviews)
    
    print("\n" + "="*40)
    print(f"📊 ANALYSIS RESULT: {movie_name.capitalize()}")
    print("="*40)
    print(f"✅ Positive Reactions: {pos_count} ({pos_count/total*100:.1f}%)")
    print(f"❌ Negative Reactions: {neg_count} ({neg_count/total*100:.1f}%)")
    print("-" * 40)
    
    # 개별 리뷰 분석 결과 보여주기 (옵션)
    print("\n🔍 Sample Insights:")
    for i, (review, sentiment) in enumerate(zip(reviews[:3], predictions[:3])):
        icon = "😊" if sentiment == "positive" else "😠"
        print(f"   {icon} [{sentiment.upper()}] \"{review}\"")
    
    # 4. 워드클라우드 생성
    print("\n☁️  Generating Word Cloud...")
    generate_wordcloud(reviews, key)
    print("="*40 + "\n")

# ==========================================
# 3. 메인 실행부 (Entry Point)
# ==========================================

if __name__ == "__main__":
    # 명령어 인자 설정 (CLI)
    parser = argparse.ArgumentParser(description="Sentinema: AI-based Movie Review Analyzer")
    parser.add_argument("--movie", type=str, help="Name of the movie to analyze (e.g., Inception)")
    
    args = parser.parse_args()

    if args.movie:
        analyze_movie(args.movie)
    else:
        # 영화 이름을 입력하지 않았을 때 안내 메시지
        print("\n👋 Welcome to Sentinema CLI!")
        print("   Usage: python main.py --movie \"Movie Name\"")
        print("   Example: python main.py --movie \"Parasite\"")
        print("\n   Available demo movies: Inception, Parasite, Joker")
