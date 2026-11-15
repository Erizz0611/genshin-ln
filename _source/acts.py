# Dữ liệu dùng chung cho PDF (make.py) và web (web_build.py).
# Thêm màn mới: viết file nguồn manX.txt rồi thêm 1 mục vào ACTS bên dưới.
LUMINE = dict(name='Lumine', role='Nhân vật chính · Nhà Lữ Hành', img='lumine_icon.png',
  desc='Nhà Lữ Hành đến từ thế giới khác. Bị vị thần lạ mặt phong ấn và cướp mất người anh song sinh, cô bắt đầu hành trình đi tìm Bảy Vị Thần của Teyvat.')
PAIMON = dict(name='Paimon', role='Bạn đồng hành', img='paimon.png', desc='Được Lumine cứu khỏi chết đuối hai tháng trước, Paimon tự nhận làm người dẫn đường cho cô. Hay ăn, hay nói, và rất ghét bị gọi là “thực phẩm dự trữ”.')
AETHER = dict(name='Aether', role='Anh trai song sinh của Lumine', desc='Bị vị thần lạ mặt mang đi trong ngày hai anh em định rời khỏi thế giới này. Là người mà Lumine đang tìm kiếm.')
GOD = dict(name='Vị Thần Lạ Mặt', role='Bí ẩn', desc='Tự xưng là “người duy trì thiên lý”. Đã chặn đường cặp song sinh, phong ấn Lumine và đem Aether đi.')
AMBER = dict(name='Amber', role='Kỵ Sĩ Trinh Thám · Đội Kỵ Sĩ Tây Phong', img='amber_icon.png', desc='Cô gái nhiệt huyết, Kỵ Sĩ Trinh Thám cuối cùng của Đội Kỵ Sĩ. Gặp Lumine trên đường đến Mondstadt, đã hộ tống cô vào thành và tặng cô Phong Chi Dực.')
KAEYA = dict(name='Kaeya', role='Đội Trưởng Kỵ Binh · Đội Kỵ Sĩ Tây Phong', img='kaeya_icon.png', desc='Kiếm sĩ có vẻ ngoài ngoại quốc với miếng bịt mắt, lời nói luôn nửa đùa nửa thật. Đã chứng kiến Lumine đẩy lui Phong Ma Long.')
JEAN = dict(name='Jean', role='Đội Trưởng Đại Diện · Đội Kỵ Sĩ Tây Phong', img='jean_icon.png', desc='“Người Thủ Hộ Mondstadt”, đang gánh vác Đội Kỵ Sĩ khi đại đội trưởng đi xa. Người lên kế hoạch thanh lý ba ngôi đền Tứ Phong Thủ Hộ.')
LISA = dict(name='Lisa', role='Quản lý thư viện · Đội Kỵ Sĩ Tây Phong', img='lisa_icon.png', desc='Ma pháp sư thông thái nhưng có phần biếng nhác. Nhờ ma pháp của cô mà Đội Kỵ Sĩ tìm ra nguồn gốc cơn bão.')
DRAGON = dict(name='Phong Ma Long', role='Mối đe dọa của Mondstadt', img='dvalin_icon.png', desc='Con rồng khổng lồ màu xanh thường xuất hiện quanh Mondstadt, gây ra bão tố và tấn công thẳng vào thành.')
BOY = dict(name='Thiếu niên bí ẩn', role='Chưa rõ danh tính', desc='Người được Lumine và Paimon bắt gặp đang nói chuyện với con rồng trong rừng.')
VOICE = dict(name='Âm Thanh Thần Bí', role='Chưa rõ danh tính', desc='Giọng nói đã dùng “gió ngàn năm” nâng đỡ Lumine trong trận chiến với Phong Ma Long.')
REDHAIR = dict(name='Người đàn ông tóc đỏ', role='Chưa rõ danh tính', desc='Xuất hiện sau khi Lumine rời Đền Sói Bắc Phong, hạ gục Pháp Sư Vực Sâu trước mặt Kaeya.')
MAGE = dict(name='Pháp Sư Vực Sâu', role='Kẻ đứng sau', desc='Kẻ đã giật dây đám Hilichurl phục kích ở Đền Sói Bắc Phong.')
DVALIN = dict(name='Dvalin', role='Tên thật của Phong Ma Long', img='dvalin_icon.png', desc='Theo lời Lisa, Dvalin từng là Rồng Đông Phong trong Tứ Phong Thủ Hộ trước khi bị gọi là Ma Long.')

SERIES = 'Genshin Impact · Light Novel'
FOOT = 'Truyện chuyển thể phi thương mại từ cốt truyện Genshin Impact (HoYoverse). Lời thoại theo bản tiếng Việt chính thức của game.'


# Mỗi màn: id (dùng làm tên thư mục web), arc (phần truyện), file nguồn, nhãn, tên, phụ đề, ảnh bìa, nhân vật, tên PDF, chân trang PDF, side=True nếu là nhiệm vụ bắt buộc (Màn X.1)
ACTS = [
  dict(id='man1', arc='Mở Đầu', src='man1.txt', act='Mở Đầu · Màn 1', title='Người Phương Xa Đuổi Theo Gió', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='traveler_portrait.png', cast=[LUMINE, PAIMON, AETHER, GOD, AMBER, KAEYA, JEAN, LISA, DRAGON, BOY, VOICE],
       pdf='GenshinLN_MoDau_Man1_NguoiPhuongXaDuoiTheoGio.pdf', footer='Mở Đầu · Màn 1 — Người Phương Xa Đuổi Theo Gió', side=False),
  dict(id='man1-1', arc='Mở Đầu', src='man1_1.txt', act='Mở Đầu · Màn 1.1', title='Ba Ngôi Đền Của Tứ Phong', sub='Nhiệm vụ bắt buộc để hoàn thành Màn 1 — Amber, Kaeya, Lisa',
       hero='lisa_splash.png', cast=[LUMINE, PAIMON, AMBER, KAEYA, LISA, JEAN, REDHAIR, MAGE, DVALIN],
       pdf='GenshinLN_MoDau_Man1.1_BaNgoiDenTuPhong.pdf', footer='Mở Đầu · Màn 1.1 — Ba Ngôi Đền Của Tứ Phong', side=True),
]
