# Dữ liệu dùng chung cho PDF (make.py) và web (web_build.py).
# Thêm màn mới: viết file nguồn manX.txt rồi thêm 1 mục vào ACTS bên dưới.
LUMINE = dict(name='Lumine', role='Nhân vật chính · Nhà Lữ Hành', img='lumine_icon.png',
  desc='Nhà Lữ Hành đến từ thế giới khác. Bị vị thần lạ mặt phong ấn và cướp mất người anh song sinh, cô bắt đầu hành trình đi tìm Bảy Vị Thần của Teyvat.')
PAIMON = dict(name='Paimon', role='Bạn đồng hành', img='paimon.png', desc='Được Lumine cứu khỏi chết đuối hai tháng trước, Paimon tự nhận làm người dẫn đường cho cô. Hay ăn, hay nói, và rất ghét bị gọi là “thực phẩm dự trữ”.')
AETHER = dict(name='Aether', role='Anh trai song sinh của Lumine', img='aether_icon.png', desc='Bị vị thần lạ mặt mang đi trong ngày hai anh em định rời khỏi thế giới này. Là người mà Lumine đang tìm kiếm.')
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

VENTI = dict(name='Venti', role='Nhà thơ lang thang', img='venti_icon.png', desc='Thiếu niên mặc đồ xanh từng nói chuyện với Dvalin trong rừng. Tự xưng là nhà thơ lang thang giỏi nhất thế gian, có mối liên hệ kỳ lạ với Nguyên Tố Phong, muốn dùng Đàn Thiên Không để cứu Dvalin.')
DILUC = dict(name='Diluc', role='Chủ Tửu Trang Dawn', img='diluc_icon.png', desc='Ông chủ lớn đứng sau quán rượu Quà Tặng Của Thiên Sứ, không ưa Đội Kỵ Sĩ nhưng ra tay che giấu và giúp nhóm Lumine lấy lại Đàn Thiên Không.')
ANASTASIA = dict(name='Anastasia', role='Quan ngoại giao Fatui', desc='Sứ giả Fatui của Snezhnaya, đòi Đội Kỵ Sĩ giao việc phòng thủ Mondstadt cho Fatui nếu không thể tiêu diệt Ma Long.')
GOTELINDE = dict(name='Gotelinde', role='Tu nữ Đại Giáo Đường', desc='Tu nữ từ chối cho Venti và Lumine mượn Đàn Thiên Không khi không có văn bản xác nhận.')
SIGNORA = dict(name='Signora', role='Quan Chấp Hành thứ 8 của Fatui', desc='Chỉ được nhắc đến qua lời đe dọa của thủ vệ Fatui và lời giải thích của Diluc. Chưa xuất hiện trực tiếp.')
MAGE2 = dict(name='Pháp Sư Vực Sâu', role='Giáo Đoàn Vực Sâu', desc='Kẻ dùng lời nguyền ăn mòn tâm trí Dvalin, phá hỏng cuộc gặp ở Vực Hái Sao và nhắc đến một kẻ mà hắn gọi là “Điện hạ”.')
DVALIN2 = dict(name='Dvalin', role='Phong Ma Long · Rồng Đông Phong', img='dvalin_icon.png', desc='Nước mắt của nó kết tinh thành những viên đá đỏ. Theo Venti, nó bị máu độc của ác long và lời nguyền Vực Sâu hành hạ, chứ không tự sinh ra thù hận.')

# --- Màn 3 ---
VENTI3 = dict(name='Venti', role='Nhà thơ lang thang · Phong Thần Barbatos', img='venti_icon.png', desc='Nhà thơ lang thang, cũng chính là Phong Thần Barbatos. Tự nhận mình là “người yếu nhất trong bảy vị thần”, dẫn sức mạnh Nguyên Tố Phong cho Lumine trong trận chiến cứu Dvalin.')
DILUC3 = dict(name='Diluc', role='Chủ Tửu Trang Dawn', img='diluc_icon.png', desc='Dùng mạng lưới tình báo tìm ra dấu vết Pháp Sư Vực Sâu gần Tửu Trang, rồi cùng nhóm Lumine tiến vào Phế Tích Phong Long.')
JEAN3 = dict(name='Jean', role='Đội Trưởng Đại Diện · Đội Kỵ Sĩ Tây Phong', img='jean_icon.png', desc='Sẵn sàng làm “kỵ sĩ xung phong lên trước”, cùng Lumine vào Phế Tích Phong Long và đứng ra giải thích hiểu lầm về Dvalin cho người dân.')
DVALIN3 = dict(name='Dvalin', role='Phong Ma Long · Rồng Đông Phong', img='dvalin_icon.png', desc='Bị lời nguyền Vực Sâu thao túng, rút về sào huyệt ở Phế Tích Phong Long. Được Lumine giải thoát và Venti chúc phúc để “bay tự do thêm nữa”.')
MAGE3 = dict(name='Pháp Sư Vực Sâu', role='Giáo Đoàn Vực Sâu', desc='Kẻ cản trở cuộc gặp ở Vực Hái Sao, bị nhóm Lumine săn lùng và hạ gục gần Tửu Trang.')
AMBER3 = dict(name='Amber', role='Kỵ Sĩ Trinh Thám · Đội Kỵ Sĩ Tây Phong', img='amber_icon.png', desc='Ở lại giữ Mondstadt trước cuộc tấn công bất thường của Hilichurl, rồi mời Lumine ăn Thịt Nướng Mật Ong mừng chiến thắng.')
KAEYA3 = dict(name='Kaeya', role='Đội Trưởng Kỵ Binh · Đội Kỵ Sĩ Tây Phong', img='kaeya_icon.png', desc='Âm thầm cố thủ trong thành, đánh kẻ xâm nhập của Giáo Đoàn Vực Sâu và biết được chúng có một kẻ chỉ đạo gọi là “Hoàng tử điện hạ”.')
BARBARA = dict(name='Barbara', role='Mục sư tế lễ · Giáo hội Tây Phong', img='barbara_icon.png', desc='Chuyên viên phụ trách thu hồi Đàn Thiên Không của giáo hội. Đã chữa trị cho Lumine và Venti khi hai người bất tỉnh bên ngoài Giáo Đường.')
SIGNORA3 = dict(name='Signora', role='Quan Chấp Hành thứ 8 của Fatui', img='signora_icon.png', desc='Phục kích Venti bên ngoài Đại Giáo Đường và cướp đi Gnosis của Phong Thần.')

# --- Chương 1 Màn 1 (Liyue) ---
CHILDE = dict(name='Childe', role='Quan Chấp Hành Fatui', img='childe_icon.png', desc='Chàng trai trẻ đã kéo Lumine thoát khỏi vòng vây Thiên Nham Quân. Tự nhận là Quan Chấp Hành Fatui, đưa cho cô tín vật để đi tìm tiên nhân ở Tuyệt Vân Gián.')
NINGGUANG = dict(name='Ningguang', role='“Thiên Quyền” của Thất Tinh Liyue', img='ningguang_icon.png', desc='Người chủ trì Điển Lễ Thỉnh Tiên. Khi tiên thể của Đế Quân rơi xuống, cô ra lệnh bao vây toàn bộ Ngọc Kinh Đài.')
REX = dict(name='Nham Vương Đế Quân', role='Nham Thần Morax', desc='Vị thần lâu đời nhất trong bảy vị thần, thần của khế ước. Tiên thể của ngài rơi xuống đài tế giữa Điển Lễ Thỉnh Tiên, không còn hơi thở.')
MOONCARVER = dict(name='Tước Nguyệt Trúc Dương Chân Quân', role='Tiên nhân ở Tuyệt Vân Gián', desc='Tam Nhãn Ngũ Hiển Tiên Nhân đầu tiên Lumine gặp. Đẩy lui Thiên Nham Quân rồi nhờ cô đi báo tin cho các tiên nhân khác.')
XIAO = dict(name='Xiao', role='Hộ Pháp Dạ Xoa · Hàng Ma Đại Thánh', img='xiao_icon.png', desc='Tiên nhân xuất hiện ở Nhà Trọ Vọng Thư. Lạnh lùng xua người trần đi, nhưng thích món đậu hũ hạnh nhân.')
GOLDET = dict(name='Verr Goldet', role='Chủ Nhà Trọ Vọng Thư', desc='Người Mondstadt làm chủ nhà trọ. Chỉ cho Lumine cách “dỗ Xiao vui vẻ” và cách đối phó với hồn ma trong quán.')
YANXIAO = dict(name='Yanxiao', role='Đầu bếp Nhà Trọ Vọng Thư', desc='Đầu bếp trông dữ tợn nhưng sợ ma, chỉ chịu làm đậu hũ hạnh nhân sau khi hồn ma hứa không quậy nữa.')
MING = dict(name='Bé Ming', role='Hồn ma nhỏ ở nhà trọ', desc='Linh hồn cô bé hay hát, trêu chọc khách trọ cho đến khi bị Lumine bắt được.')
MOUNTAIN = dict(name='Lí Thủy Điệp Sơn Chân Quân', role='Tiên nhân ở Hổ Lao Sơn', desc='Vị tiên nhân trồng hoa “Đạc Sơn Quy” sinh ra Hổ Phách để giữ sơn môn thanh tịnh.')
CLOUD = dict(name='Lưu Vân Tá Phong Chân Quân', role='Tiên nhân ở Âu Tàng Sơn', desc='Vị tiên nhân giỏi “cơ quan thuật”, suýt đi “trấn áp” Cảng Liyue khi nghe tin Đế Quân bị ám sát.')
LIDING = dict(name='Li Ding và Li Dang', role='Hai anh em lên Hổ Lao Sơn', desc='Lên núi tìm bảo vật trong Hổ Phách, một người bị Hổ Phách nhốt lại và được Lumine cứu ra.')


# --- Chương 1 Màn 2 (Liyue) ---
ZHONGLI = dict(name='Zhongli', role='Khách của Vãng Sinh Đường', img='zhongli_icon.png', desc='Người “trong nghề” được Childe giới thiệu. Am hiểu mọi phong tục của Liyue nhưng luôn quên mang tiền, mời Lumine cùng chuẩn bị Điển Lễ Tiễn Tiên cho Nham Vương Đế Quân.')
CHILDE2 = dict(name='Childe', role='Quan Chấp Hành Fatui', img='childe_icon.png', desc='Giữ lời hứa tìm “người có thể phá vỡ cục diện”, chi tiền cho Điển Lễ Tiễn Tiên, nhưng âm thầm cho người nghe ngóng chuyện Hoàng Kim Ốc.')
EKATERINA = dict(name='Ekaterina', role='Nhân viên Ngân hàng Bắc Quốc', desc='Người của Fatui ở quầy Ngân hàng Bắc Quốc, chỉ đường cho Lumine đến Lưu Ly Đình và nghe lén giúp Childe.')
SHITOU = dict(name='Shitou', role='Chủ tiệm ngọc Giải Thúy Hàng', desc='Ông chủ tiệm ngọc keo kiệt, nhưng chỉ lấy nửa giá rương Dạ Phách Thạch khi biết nó dùng để tiễn Nham Vương Gia.')
YINGER = dict(name="Ying'er", role='Người làm Sáp Thơm ở Xuân Hương Diêu', desc='Cô gái hay trêu chọc, đã cùng Lumine nấu ba loại Sáp Thơm từ Hoa Nghê Thường ở bếp Vạn Dân Đường.')
PING = dict(name='Bình Lão Lão', role='Người giữ Chuông Tẩy Trần', desc='Bà lão sống trên Ngọc Kinh Đài, cất “tất cả tài sản” trong một chiếc ấm thần kỳ. Bạn cũ của Zhongli.')
QIQI = dict(name='Qiqi', role='Nhân viên Nhà Thuốc Bubu', img='qiqi_icon.png', desc='Cô bé cương thi chỉ hành động theo “mệnh lệnh” tự đặt cho mình, nhờ nhóm Lumine đi bắt “Dê Dừa” để đổi lấy Hương Bất Tử.')
BAIZHU = dict(name='Baizhu', role='Chủ Nhà Thuốc Bubu', img='baizhu_icon.png', desc='Ông chủ nhà thuốc cùng con rắn biết nói Changsheng. Bán Hương Bất Tử giá 299 vạn Mora sau khi bắt tay với Childe.')
GANYU = dict(name='Ganyu', role='Thư ký Nguyệt Hải Đình', img='ganyu_icon.png', desc='Thư ký của toàn thể Thất Tinh, sứ giả đặc biệt của Ningguang. Tìm đến quán Ba Cốc Say Mèm để trao thư mời Lumine đến Quần Ngọc Các.')

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
  dict(id='man2', arc='Mở Đầu', src='man2.txt', act='Mở Đầu · Màn 2', title='Vì Một Ngày Mai Không Rơi Lệ', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='venti_splash.png', cast=[LUMINE, PAIMON, VENTI, JEAN, DILUC, LISA, DVALIN2, MAGE2, ANASTASIA, GOTELINDE, SIGNORA],
       pdf='', footer='Mở Đầu · Màn 2 — Vì Một Ngày Mai Không Rơi Lệ', side=False),
  dict(id='man3', arc='Mở Đầu', src='man3.txt', act='Mở Đầu · Màn 3', title='Bài Ca Về Rồng Và Tự Do', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='dvalin_wide.png', cast=[LUMINE, PAIMON, VENTI3, JEAN3, DILUC3, DVALIN3, MAGE3, AMBER3, KAEYA3, BARBARA, SIGNORA3],
       pdf='', footer='Mở Đầu · Màn 3 — Bài Ca Về Rồng Và Tự Do', side=False),
  dict(id='c1-man1', arc='Chương 1 · Liyue', src='c1_man1.txt', act='Chương 1 Màn 1', title='Phù Thế Phù Sinh Thiên Nham Gian', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='childe_card.png', cast=[LUMINE, PAIMON, CHILDE, NINGGUANG, REX, MOONCARVER, XIAO, GOLDET, YANXIAO, MING, MOUNTAIN, CLOUD, LIDING],
       pdf='', footer='Chương 1 Màn 1 — Phù Thế Phù Sinh Thiên Nham Gian', side=False),
  dict(id='c1-man2', arc='Chương 1 · Liyue', src='c1_man2.txt', act='Chương 1 Màn 2', title='Lời Tạm Biệt Thể Xác Vĩnh Hằng', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='zhongli_card.png', cast=[LUMINE, PAIMON, ZHONGLI, CHILDE2, PING, QIQI, BAIZHU, GANYU, EKATERINA, SHITOU, YINGER],
       pdf='', footer='Chương 1 Màn 2 — Lời Tạm Biệt Thể Xác Vĩnh Hằng', side=False),
]
