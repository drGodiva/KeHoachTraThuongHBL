import streamlit as st

# CẤU HÌNH TRANG VÀ MÀU SẮC (Xanh Ngọc Lục Bảo & Vàng Kim)
st.set_page_config(page_title="Đào Tạo KHTT - Phụng Tâm", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F4FBF9; }
    h1, h2, h3 { color: #004D40 !important; }
    .emerald { color: #004D40; font-weight: bold; }
    .gold { color: #D4AF37; font-weight: bold; }
    .box { background: white; padding: 20px; border-radius: 10px; border-left: 8px solid #D4AF37; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# GIAO DIỆN CHÍNH
st.title("🌟 HỆ THỐNG PHỤNG TÂM: BẢN ĐỒ KẾ HOẠCH TRẢ THƯỞNG")
st.markdown("---")

# THANH ĐIỀU HƯỚNG BÊN TRÁI
menu = st.sidebar.radio("📚 DANH MỤC GIẢNG DẠY", 
    ["1. Chiết Khấu & Thăng Cấp (25%-50%)", 
     "2. Khái Niệm & Tái Đạt Chuẩn", 
     "3. Nấc Thang Lãnh Đạo (Đến Chủ Tịch)", 
     "4. Kim Cương & Mark Hughes Bonus"])

# ==========================================
# PHẦN 1: CHIẾT KHẤU 25% - 50%
# ==========================================
if menu == "1. Chiết Khấu & Thăng Cấp (25%-50%)":
    st.header("1. HÀNH TRÌNH CHIẾT KHẤU (25% - 50%)")
    st.image("https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=1000&q=80", caption="Bước đệm vững chắc cho doanh nghiệp của bạn")
    
    tab25, tab35, tab42, tab50 = st.tabs(["🥉 25% (Thành Viên)", "🥈 35% (Tư Vấn Viên CC)", "🥇 42% (Cấp Quản Lý)", "🏆 50% (Giám Sát Viên)"])
    
    with tab25:
        st.markdown("""
        <div class="box">
            <h3>🥉 Cấp bậc: THÀNH VIÊN</h3>
            <ul>
                <li><b>Điều kiện điểm:</b> <span class="gold">0 Điểm</span></li>
                <li><b>Ai mua:</b> Không yêu cầu.</li>
                <li><b>Thời gian:</b> Ngay khi ký hợp đồng.</li>
                <li><b>Quyền lợi:</b> Mua hàng chiết khấu 25%.</li>
                <li><b>Thời hạn:</b> <span class="emerald">Vĩnh viễn (Không cần tái đạt chuẩn hàng năm)</span></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with tab35:
        st.markdown("""
        <div class="box">
            <h3>🥈 Cấp bậc: TƯ VẤN VIÊN CAO CẤP</h3>
            <ul>
                <li><b>Điều kiện điểm:</b> <span class="gold">500 Điểm</span></li>
                <li><b>Ai mua:</b> Tổng Doanh số Trực tiếp (bạn tự mua) + Doanh số Tuyến dưới.</li>
                <li><b>Thời gian:</b> Tích lũy trong 1 đến 2 tháng liên tiếp.</li>
                <li><b>Quyền lợi:</b> Chiết khấu 35% + Hưởng 10% Lợi nhuận bán sỉ từ tuyến dưới (25%).</li>
                <li><b>Thời hạn:</b> <span class="emerald">Vĩnh viễn (Không cần tái đạt chuẩn hàng năm)</span></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with tab42:
        st.markdown("""
        <div class="box">
            <h3>🥇 ĐƯỜNG 1: NHÀ KIẾN TẠO THÀNH CÔNG (Đường Nhanh)</h3>
            <ul>
                <li><b>Điều kiện điểm:</b> <span class="gold">1.000 Điểm</span></li>
                <li><b>Ai mua:</b> Trực tiếp + Tuyến dưới.</li>
                <li><b>Thời gian:</b> 1 đến 3 tháng liên tiếp.</li>
                <li><b>Quyền lợi:</b> Chiết khấu 42% + 17% Lợi nhuận bán sỉ.</li>
                <li><b>Thời hạn:</b> <span class="emerald">Vĩnh viễn</span></li>
            </ul>
        </div>
        <div class="box">
            <h3>🥇 ĐƯỜNG 2: NGƯỜI BÁN HÀNG ĐẠT CHUẨN (Đường Dài)</h3>
            <ul>
                <li><b>Điều kiện điểm:</b> <span class="gold">2.500 Điểm</span></li>
                <li><b>Ai mua:</b> Phải có tối thiểu <b>500 điểm Trực tiếp</b> (tự mua), còn lại từ Tuyến dưới.</li>
                <li><b>Thời gian:</b> 1 đến 6 tháng liên tiếp.</li>
                <li><b>Quyền lợi:</b> Tương tự đường nhanh.</li>
                <li><b>Thời hạn:</b> <span class="emerald">Vĩnh viễn</span></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with tab50:
        st.markdown("""
        <div class="box">
            <h3>🏆 Cấp bậc: GIÁM SÁT VIÊN (Có 3 phương pháp)</h3>
            <ul>
                <li><b>CÁCH 1 (1 Tháng):</b> Đạt 4.000 Điểm (Bắt buộc có 1.000 Điểm chưa sử dụng).</li>
                <li><b>CÁCH 2 (2 Tháng):</b> Tích lũy 4.000 Điểm trong 2 tháng (Bắt buộc có 1.000 Điểm chưa sử dụng).</li>
                <li><b>CÁCH 3 (Cộng dồn 3-12 Tháng):</b> Đạt 4.000 Điểm. Bắt buộc có tối thiểu 1.000 điểm Trực tiếp. Tối đa mượn 3.000 điểm từ tuyến dưới.</li>
                <li><hr></li>
                <li><b>Quyền lợi:</b> Chiết khấu 50% + Lên tới 25% Bán sỉ + Hoa hồng Lãnh đạo (1-5%).</li>
                <li><b>Thời hạn:</b> <span class="gold">Phải Tái Đạt Chuẩn Hàng Năm (Nếu không sẽ bị hạ cấp).</span></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# PHẦN 2: TÁI ĐẠT CHUẨN & KHÁI NIỆM
# ==========================================
elif menu == "2. Khái Niệm & Tái Đạt Chuẩn":
    st.header("2. KHOẢNG THỜI GIAN & TÁI ĐẠT CHUẨN")
    
    with st.expander("📅 NĂM TÀI CHÍNH & THÁNG DOANH SỐ LÀ GÌ?"):
        st.info("""
        - **Tháng Doanh Số:** Tính từ ngày làm việc ĐẦU TIÊN đến ngày làm việc CUỐI CÙNG của tháng. Đơn hàng phải thanh toán trong tháng đó.
        - **Năm Tài Chính:** Bắt đầu từ **1/2 năm trước** đến hết ngày **31/1 năm sau**. Dùng để xác định giai đoạn tái đạt chuẩn GSV.
        """)
        
    with st.expander("🛡️ TÁI ĐẠT CHUẨN GIÁM SÁT VIÊN (BẮT BUỘC HÀNG NĂM)"):
        st.warning("""
        Để giữ quyền lợi 50% và hệ thống, GSV phải tái đạt chuẩn mỗi Năm Tài Chính bằng 1 trong các cách:
        1. **Một tháng:** 4.000 Điểm (Tối thiểu 1.000 Chưa sử dụng).
        2. **Hai tháng:** 4.000 Điểm trong 2 tháng liên tiếp (Tối thiểu 1.000 Chưa sử dụng).
        3. **Tích lũy 12 tháng (Giữ tuyến dưới):** 10.000 Điểm Tổng Doanh Số Chưa Sử Dụng.
        4. **Tích lũy 12 tháng (Mất tuyến dưới):** 2.000 Điểm Chưa Sử Dụng. (Bạn vẫn giữ 50%, nhưng TOÀN BỘ nhánh tuyến dưới có GSV sẽ bị đẩy lên cho tuyến trên).
        """)

# ==========================================
# PHẦN 3: NẤC THANG LÃNH ĐẠO
# ==========================================
elif menu == "3. Nấc Thang Lãnh Đạo (Đến Chủ Tịch)":
    st.header("3. NẤC THANG LÃNH ĐẠO & NHÓM TAB")
    st.image("https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=1000&q=80", caption="Tiến vào Nhóm Thành Tích Cao Nhất")
    
    st.markdown("""
    <div class="box">
        <h3>🌍 1. Nhóm Thế Giới (World Team)</h3>
        <p><b>Điều kiện:</b> 2.500 TV mỗi tháng x 4 tháng liên tiếp; HOẶC 10.000 TV x 1 tháng; HOẶC 500 RO x 1 tháng.</p>
    </div>
    <div class="box">
        <h3>🌟 2. Nhóm Phát Triển Toàn Cầu (GET) & GET 2500</h3>
        <p><b>GET:</b> 1.000 RO mỗi tháng x 3 tháng liên tiếp. (Quyền lợi: Hưởng thêm 2% Hoa hồng Doanh số).</p>
        <p><b>GET 2500:</b> 2.500 RO mỗi tháng x 3 tháng liên tiếp.</p>
    </div>
    <div class="box">
        <h3>💼 3. Nhóm Triệu Phú (Millionaire Team) & Triệu Phú 7500</h3>
        <p><b>Triệu Phú:</b> 4.000 RO mỗi tháng x 3 tháng liên tiếp. (Quyền lợi: Hưởng thêm đến 4% Hoa hồng Doanh số).</p>
        <p><b>Triệu Phú 7500:</b> 7.500 RO mỗi tháng x 3 tháng liên tiếp.</p>
    </div>
    <div class="box">
        <h3>👑 4. Nhóm Chủ Tịch (President's Team) & Các Mốc (15K - 140K)</h3>
        <p><b>Chủ Tịch:</b> 10.000 RO mỗi tháng x 3 tháng liên tiếp. (Quyền lợi: Hưởng thêm đến 7% Hoa hồng Doanh số).</p>
        <p><b>Chủ Tịch 15K đến 140K:</b> Đạt từ 15.000 RO đến 140.000 RO mỗi tháng trong 3 tháng liên tiếp.</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# PHẦN 4: KIM CƯƠNG & MARK HUGHES
# ==========================================
elif menu == "4. Kim Cương & Mark Hughes Bonus":
    st.header("4. ĐỈNH CAO DANH VỌNG: KIM CƯƠNG & MARK HUGHES")
    st.image("https://images.unsplash.com/photo-1599839619722-39751411ea63?auto=format&fit=crop&w=1000&q=80", caption="Ghi nhận thành tựu kiệt xuất")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="box">
            <h3 class="emerald">💎 DANH HIỆU KIM CƯƠNG</h3>
            <p>Xác định bằng số lượng Thành Viên Nhóm Chủ Tịch ở các NHÁNH RIÊNG BIỆT tuyến dưới:</p>
            <ul>
                <li><b>1 Kim Cương:</b> 1 nhánh có Chủ Tịch.</li>
                <li><b>2 Kim Cương:</b> 2 nhánh có Chủ Tịch.</li>
                <li><b>3 Kim Cương (QT):</b> 3 nhánh có Chủ Tịch.</li>
                <li><b>4 Kim Cương (LĐ):</b> 4 nhánh có Chủ Tịch.</li>
                <li><b>5 -> 9 Kim Cương:</b> 5 đến 9 nhánh có Chủ Tịch (Câu Lạc Bộ Chủ Tịch).</li>
                <li><b>10 Kim Cương:</b> 10 nhánh riêng biệt (Nhóm Sáng Lập).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="box">
            <h3 class="gold">🌐 PHẦN THƯỞNG MARK HUGHES</h3>
            <ul>
                <li><b>Nguồn quỹ:</b> Trích 1% doanh thu toàn cầu (tính trên Cơ Sở Thu Nhập) của tập đoàn.</li>
                <li><b>Đối tượng:</b> Dành riêng cho các Thành Viên xuất sắc đạt chuẩn thuộc <b>Nhóm Chủ Tịch</b>.</li>
                <li><b>Mục đích:</b> Ghi nhận thành tích nổi bật trong việc thúc đẩy kinh doanh.</li>
                <li><b>Kỳ xét duyệt:</b> Thời gian xét chuẩn là 12 tháng, bắt đầu từ <b>tháng 1 và kết thúc vào tháng 12</b> của năm đó.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)