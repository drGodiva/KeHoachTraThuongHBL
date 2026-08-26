import streamlit as st

# 1. Cấu hình trang và thiết lập màu sắc thương hiệu
st.set_page_config(page_title="Ma Trận KHTT - Phụng Tâm", page_icon="💎", layout="centered")

st.markdown("""
    <style>
    /* Nền trang web */
    .stApp {
        background-color: #F4FBF9; 
    }
    /* Tiêu đề chính - Màu Xanh Ngọc Lục Bảo */
    h1, h2, h3 {
        color: #004D40 !important; 
        text-align: center;
    }
    /* Thẻ thông tin nổi bật - Viền Vàng Kim */
    .info-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 8px solid #D4AF37;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    .thuong-hieu {
        color: #004D40;
        font-weight: bold;
        font-size: 20px;
    }
    .vang-kim {
        color: #D4AF37;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Tiêu đề và Hình ảnh (Nếu có logo, Thầy để file logo.png cùng thư mục và mở khóa dòng dưới)
# st.image("logo.png", use_container_width=True)

st.title("ĐƯỜNG TỚI PRESIDENT'S TEAM")
st.markdown("### TRUY VẤN MA TRẬN CHIẾT KHẤU")
st.markdown("---")

# 3. Nút bấm chọn mức chiết khấu
muc_tieu = st.radio(
    "👉 BẠN ĐANG MỤC TIÊU MỨC CHIẾT KHẤU NÀO?",
    ('Khởi động: 35%', 'Tăng tốc: 42%', 'Lãnh đạo: 50% (Giám Sát Viên)')
)

# 4. Hiển thị kết quả trực quan
if muc_tieu == 'Khởi động: 35%':
    st.markdown("""
    <div class="info-box">
        <div class="thuong-hieu">ĐÍCH ĐẾN: 35% (Tư Vấn Viên Cao Cấp)</div>
        <ul>
            <li><b>Cần bao nhiêu điểm?</b> <span class="vang-kim">500 Điểm</span></li>
            <li><b>Trong bao lâu?</b> Tích lũy 1 đến 2 tháng liên tiếp.</li>
            <li><b>Do ai mua?</b> Bạn tự mua hoặc tuyến dưới mua đều được.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif muc_tieu == 'Tăng tốc: 42%':
    st.markdown("""
    <div class="info-box">
        <div class="thuong-hieu">ĐÍCH ĐẾN: 42% (Nhà Kiến Tạo Thành Công) - Đường Nhanh</div>
        <ul>
            <li><b>Cần bao nhiêu điểm?</b> <span class="vang-kim">1.000 Điểm</span></li>
            <li><b>Trong bao lâu?</b> 1 đến 3 tháng liên tiếp.</li>
            <li><b>Do ai mua?</b> Bạn tự mua hoặc tuyến dưới mua.</li>
        </ul>
    </div>
    <div class="info-box">
        <div class="thuong-hieu">ĐÍCH ĐẾN: 42% (Người Bán Hàng Đạt Chuẩn) - Đường Tích Lũy</div>
        <ul>
            <li><b>Cần bao nhiêu điểm?</b> <span class="vang-kim">2.500 Điểm</span></li>
            <li><b>Trong bao lâu?</b> 1 đến 6 tháng liên tiếp.</li>
            <li><b>Do ai mua?</b> Bắt buộc BẠN TỰ MUA tối thiểu 500 điểm, phần còn lại có thể từ tuyến dưới.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="info-box">
        <div class="thuong-hieu">ĐÍCH ĐẾN: 50% (Giám Sát Viên) - Chạy Tốc Lực</div>
        <ul>
            <li><b>Cần bao nhiêu điểm?</b> <span class="vang-kim">4.000 Điểm</span></li>
            <li><b>Trong bao lâu?</b> 1 tháng HOẶC 2 tháng liên tiếp.</li>
            <li><b>Do ai mua?</b> Bắt buộc phải có <span class="vang-kim">1.000 điểm Chưa Sử Dụng</span> (Không bị tuyến dưới dùng để lên 50%).</li>
        </ul>
    </div>
    <div class="info-box">
        <div class="thuong-hieu">ĐÍCH ĐẾN: 50% (Giám Sát Viên) - Đường Dài</div>
        <ul>
            <li><b>Cần bao nhiêu điểm?</b> <span class="vang-kim">4.000 Điểm</span></li>
            <li><b>Trong bao lâu?</b> 3 đến 12 tháng.</li>
            <li><b>Do ai mua?</b> Bắt buộc BẠN TỰ MUA tối thiểu 1.000 điểm. Tuyến dưới đóng góp tối đa 3.000 điểm.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.success("Khi bạn giúp người khác đạt 50%, bạn bắt đầu hành trình xây dựng sự thịnh vượng vô hạn!")