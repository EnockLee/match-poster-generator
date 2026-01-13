import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# ==================================================
# 基础配置
# ==================================================
BASE_IMAGE = "base.png"
CSV_FILE = "schedule.csv"
OUTPUT_DIR = "out"

# 固定坐标（110 方案）
DATE_POS = (600, 120)
HOME_POS = (600, 340)
AWAY_POS = (600, 520)

# 字体设置
FONT_DATE = ImageFont.truetype(
    "fonts/SourceHanSansCN-Regular.otf", 84
)
FONT_TEAM = ImageFont.truetype(
    "fonts/SourceHanSansCN-Medium.otf", 110
)

# 颜色与描边
TEXT_COLOR = (255, 255, 255)   # 白字
STROKE_COLOR = (0, 0, 0)       # 黑描边
STROKE_WIDTH = 2               # 描边粗细（110 时不建议再大）

# ==================================================
# 工具函数：带描边文字
# ==================================================
def draw_text_with_stroke(draw, pos, text, font):
    x, y = pos

    # 先画描边（8 向偏移）
    for dx in range(-STROKE_WIDTH, STROKE_WIDTH + 1):
        for dy in range(-STROKE_WIDTH, STROKE_WIDTH + 1):
            if dx == 0 and dy == 0:
                continue
            draw.text(
                (x + dx, y + dy),
                text,
                font=font,
                fill=STROKE_COLOR
            )

    # 再画正文
    draw.text(
        (x, y),
        text,
        font=font,
        fill=TEXT_COLOR
    )

# ==================================================
# 主流程
# ==================================================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = pd.read_csv(CSV_FILE)

    for idx, row in df.iterrows():
        img = Image.open(BASE_IMAGE).convert("RGBA")
        draw = ImageDraw.Draw(img)

        date_text = str(row["date"])
        home_text = str(row["home"])
        away_text = str(row["away"])

        # 绘制文本
        draw_text_with_stroke(draw, DATE_POS, date_text, FONT_DATE)
        draw_text_with_stroke(draw, HOME_POS, home_text, FONT_TEAM)
        draw_text_with_stroke(draw, AWAY_POS, away_text, FONT_TEAM)

        # 输出文件名（规避非法字符）
        safe_date = (
            date_text
            .replace("/", "-")
            .replace(":", "-")
            .replace(" ", "_")
        )
        output_path = f"{OUTPUT_DIR}/{safe_date}_{idx}.png"

        img.save(output_path)
        print(f"生成完成：{output_path}")

    print("✅ 全部赛程图片生成完毕")

if __name__ == "__main__":
    main()
