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

# --- Màn III ---
VENTI3 = dict(name='Venti', role='Nhà thơ lang thang · Phong Thần Barbatos', img='venti_icon.png', desc='Nhà thơ lang thang, cũng chính là Phong Thần Barbatos. Tự nhận mình là “người yếu nhất trong bảy vị thần”, dẫn sức mạnh Nguyên Tố Phong cho Lumine trong trận chiến cứu Dvalin.')
DILUC3 = dict(name='Diluc', role='Chủ Tửu Trang Dawn', img='diluc_icon.png', desc='Dùng mạng lưới tình báo tìm ra dấu vết Pháp Sư Vực Sâu gần Tửu Trang, rồi cùng nhóm Lumine tiến vào Phế Tích Phong Long.')
JEAN3 = dict(name='Jean', role='Đội Trưởng Đại Diện · Đội Kỵ Sĩ Tây Phong', img='jean_icon.png', desc='Sẵn sàng làm “kỵ sĩ xung phong lên trước”, cùng Lumine vào Phế Tích Phong Long và đứng ra giải thích hiểu lầm về Dvalin cho người dân.')
DVALIN3 = dict(name='Dvalin', role='Phong Ma Long · Rồng Đông Phong', img='dvalin_icon.png', desc='Bị lời nguyền Vực Sâu thao túng, rút về sào huyệt ở Phế Tích Phong Long. Được Lumine giải thoát và Venti chúc phúc để “bay tự do thêm nữa”.')
MAGE3 = dict(name='Pháp Sư Vực Sâu', role='Giáo Đoàn Vực Sâu', desc='Kẻ cản trở cuộc gặp ở Vực Hái Sao, bị nhóm Lumine săn lùng và hạ gục gần Tửu Trang.')
AMBER3 = dict(name='Amber', role='Kỵ Sĩ Trinh Thám · Đội Kỵ Sĩ Tây Phong', img='amber_icon.png', desc='Ở lại giữ Mondstadt trước cuộc tấn công bất thường của Hilichurl, rồi mời Lumine ăn Thịt Nướng Mật Ong mừng chiến thắng.')
KAEYA3 = dict(name='Kaeya', role='Đội Trưởng Kỵ Binh · Đội Kỵ Sĩ Tây Phong', img='kaeya_icon.png', desc='Âm thầm cố thủ trong thành, đánh kẻ xâm nhập của Giáo Đoàn Vực Sâu và biết được chúng có một kẻ chỉ đạo gọi là “Hoàng tử điện hạ”.')
BARBARA = dict(name='Barbara', role='Mục sư tế lễ · Giáo hội Tây Phong', img='barbara_icon.png', desc='Chuyên viên phụ trách thu hồi Đàn Thiên Không của giáo hội. Đã chữa trị cho Lumine và Venti khi hai người bất tỉnh bên ngoài Giáo Đường.')
SIGNORA3 = dict(name='Signora', role='Quan Chấp Hành thứ 8 của Fatui', img='signora_icon.png', desc='Phục kích Venti bên ngoài Đại Giáo Đường và cướp đi Gnosis của Phong Thần.')

# --- Chương I · Màn I (Liyue) ---
CHILDE = dict(name='Childe', role='Quan Chấp Hành Fatui', img='childe_icon.png', desc='Chàng trai trẻ đã kéo Lumine thoát khỏi vòng vây Thiên Nham Quân. Tự nhận là Quan Chấp Hành Fatui, đưa cho cô tín vật để đi tìm tiên nhân ở Tuyệt Vân Gián.')
NINGGUANG = dict(name='Ningguang', role='“Thiên Quyền” của Thất Tinh Liyue', img='ningguang_icon.png', desc='Người chủ trì Điển Lễ Thỉnh Tiên. Khi tiên thể của Đế Quân rơi xuống, cô ra lệnh bao vây toàn bộ Ngọc Kinh Đài.')
REX = dict(name='Nham Vương Đế Quân', role='Nham Thần Morax', desc='Vị thần lâu đời nhất trong bảy vị thần, thần của khế ước. Tiên thể của ngài rơi xuống đài tế giữa Điển Lễ Thỉnh Tiên, không còn hơi thở.')
MOONCARVER = dict(name='Tước Nguyệt Trúc Dương Chân Quân', role='Tiên nhân ở Tuyệt Vân Gián', img='mooncarver.png', desc='Tam Nhãn Ngũ Hiển Tiên Nhân đầu tiên Lumine gặp. Đẩy lui Thiên Nham Quân rồi nhờ cô đi báo tin cho các tiên nhân khác.')
XIAO = dict(name='Xiao', role='Hộ Pháp Dạ Xoa · Hàng Ma Đại Thánh', img='xiao_icon.png', desc='Tiên nhân xuất hiện ở Nhà Trọ Vọng Thư. Lạnh lùng xua người trần đi, nhưng thích món đậu hũ hạnh nhân.')
GOLDET = dict(name='Verr Goldet', role='Chủ Nhà Trọ Vọng Thư', desc='Người Mondstadt làm chủ nhà trọ. Chỉ cho Lumine cách “dỗ Xiao vui vẻ” và cách đối phó với hồn ma trong quán.')
YANXIAO = dict(name='Yanxiao', role='Đầu bếp Nhà Trọ Vọng Thư', desc='Đầu bếp trông dữ tợn nhưng sợ ma, chỉ chịu làm đậu hũ hạnh nhân sau khi hồn ma hứa không quậy nữa.')
MING = dict(name='Bé Ming', role='Hồn ma nhỏ ở nhà trọ', desc='Linh hồn cô bé hay hát, trêu chọc khách trọ cho đến khi bị Lumine bắt được.')
MOUNTAIN = dict(name='Lí Thủy Điệp Sơn Chân Quân', role='Tiên nhân ở Hổ Lao Sơn', img='mountainshaper.png', desc='Vị tiên nhân trồng hoa “Đạc Sơn Quy” sinh ra Hổ Phách để giữ sơn môn thanh tịnh.')
CLOUD = dict(name='Lưu Vân Tá Phong Chân Quân', role='Tiên nhân ở Âu Tàng Sơn', img='cloudretainer.png', desc='Vị tiên nhân giỏi “cơ quan thuật”, suýt đi “trấn áp” Cảng Liyue khi nghe tin Đế Quân bị ám sát.')
LIDING = dict(name='Li Ding và Li Dang', role='Hai anh em lên Hổ Lao Sơn', desc='Lên núi tìm bảo vật trong Hổ Phách, một người bị Hổ Phách nhốt lại và được Lumine cứu ra.')

# --- Chương I · Màn IV (Giới Thiệu + Màn IV) ---
KATHERYNE = dict(name='Katheryne', role='Hiệp Hội Nhà Mạo Hiểm Mondstadt', desc='Người tiếp tân của hiệp hội, kể cho Lumine về vị khách lạ mặt tóc vàng đeo bịt mắt vừa đến Mondstadt.')
DAIN_GT = dict(name='Dainsleif', role='Nhà mạo hiểm tự do', img='dainsleif_icon.png', desc='Người lạ mặt tóc vàng đeo bịt mắt. Nhận lời đồng hành với giá 500 Mora và ba câu hỏi, chỉ nhận ủy thác liên quan đến Giáo Đoàn Vực Sâu.')
CHARLES = dict(name='Charles', role='Người pha chế quán Quà Tặng Của Thiên Sứ', desc='Cho Lumine biết vị khách lạ “rất sành về rượu” và hẹn tối nay sẽ đến lấy rượu.')
LAWRENCE = dict(name='Lawrence và Wagner', role='Kỵ sĩ gác cổng · Thợ rèn', desc='Hai người dân Mondstadt chỉ đường cho Lumine lần theo dấu vết người lạ mặt.')
DAIN4 = dict(name='Dainsleif', img='dainsleif_icon.png', role='“Kiếm Sĩ Hoàng Hôn” của Khaenri\'ah', desc='Cùng Lumine truy tìm Sứ Đồ Vực Sâu và phá kế hoạch “lay chuyển thần tọa”. Theo lời Aether, anh là hộ vệ cung đình Khaenri\'ah đời cuối, mang lời nguyền bất tử.')
GANYU4 = dict(name='Ganyu', role='Thư ký của Thất Tinh Liyue', img='ganyu_icon.png', desc='Treo ủy thác ở hiệp hội vì lo lắng Đạo Bảo Đoàn động vào di tích của Giáo Đoàn Vực Sâu.')
LAN = dict(name='Lan', role='Hiệp Hội Nhà Mạo Hiểm Liyue', desc='Cùng Ganyu kể cho Lumine về “Nam Trưởng Tỷ”, “Bắc Quái Điểu” và “Trùm Đạo Bảo”.')
HERALD = dict(name='Sứ Đồ Vực Sâu', img='herald_icon.png', role='Giáo Đoàn Vực Sâu', desc='Thống lĩnh của Pháp Sư Vực Sâu, kẻ đứng sau kế hoạch “Máy dệt vận mệnh”. Gọi Aether là “Hoàng tử điện hạ”.')
ROSARIA = dict(name='Rosaria', role='Nữ tu Giáo Hội Tây Phong', img='rosaria_icon.png', desc='Báo tin Giáo Đoàn Vực Sâu tập họp ở Lang Lãnh.')
RAZOR = dict(name='Razor', role='Thiếu niên của bầy sói', img='razor_icon.png', desc='Bảo vệ linh hồn Vua Sói Bắc Phong trước nghi thức của Sứ Đồ Vực Sâu.')
BOREAS = dict(name='Vua Sói Bắc Phong', img='boreas_icon.png', role='Linh hồn Ma Thần Andrius · Boreas', desc='Chủ nhân Lang Lãnh. Kể về cỗ máy từng xông vào bãi tập luyện của mình — manh mối về “máy cày đầu tiên của thế giới”.')
AETHER4 = dict(name='Aether', role='Anh trai song sinh của Lumine · “Hoàng tử điện hạ”', img='aether_icon.png', desc='Xuất hiện bên cạnh Sứ Đồ Vực Sâu, gọi Dainsleif là kẻ thù và hẹn với Lumine: “Chúng ta ắt sẽ trùng phùng.”')
JEAN4 = dict(name='Jean', role='Đội Trưởng Đại Diện · Đội Kỵ Sĩ Tây Phong', img='jean_icon.png', desc='Dẫn quân đối phó Giáo Đoàn Vực Sâu ở Lang Lãnh, nhờ Lumine đi xem Vua Sói có gặp nguy hiểm không.')
BARBARA4 = dict(name='Barbara', role='Mục sư tế lễ · Giáo hội Tây Phong', img='barbara_icon.png', desc='Kể chuyện “Thất Thiên Thần Tượng mất tích” và “oán hận của bạo quân”.')


# --- Chương I · Màn II (Liyue) ---
ZHONGLI = dict(name='Zhongli', role='Khách của Vãng Sinh Đường', img='zhongli_icon.png', desc='Người “trong nghề” được Childe giới thiệu. Am hiểu mọi phong tục của Liyue nhưng luôn quên mang tiền, mời Lumine cùng chuẩn bị Điển Lễ Tiễn Tiên cho Nham Vương Đế Quân.')
CHILDE2 = dict(name='Childe', role='Quan Chấp Hành Fatui', img='childe_icon.png', desc='Giữ lời hứa tìm “người có thể phá vỡ cục diện”, chi tiền cho Điển Lễ Tiễn Tiên, nhưng âm thầm cho người nghe ngóng chuyện Hoàng Kim Ốc.')
EKATERINA = dict(name='Ekaterina', role='Nhân viên Ngân hàng Bắc Quốc', desc='Người của Fatui ở quầy Ngân hàng Bắc Quốc, chỉ đường cho Lumine đến Lưu Ly Đình và nghe lén giúp Childe.')
SHITOU = dict(name='Shitou', role='Chủ tiệm ngọc Giải Thúy Hàng', desc='Ông chủ tiệm ngọc keo kiệt, nhưng chỉ lấy nửa giá rương Dạ Phách Thạch khi biết nó dùng để tiễn Nham Vương Gia.')
YINGER = dict(name="Ying'er", role='Người làm Sáp Thơm ở Xuân Hương Diêu', desc='Cô gái hay trêu chọc, đã cùng Lumine nấu ba loại Sáp Thơm từ Hoa Nghê Thường ở bếp Vạn Dân Đường.')
PING = dict(name='Bình Lão Lão', role='Người giữ Chuông Tẩy Trần', img='ping_icon.png', desc='Bà lão sống trên Ngọc Kinh Đài, cất “tất cả tài sản” trong một chiếc ấm thần kỳ. Bạn cũ của Zhongli.')
QIQI = dict(name='Qiqi', role='Nhân viên Nhà Thuốc Bubu', img='qiqi_icon.png', desc='Cô bé cương thi chỉ hành động theo “mệnh lệnh” tự đặt cho mình, nhờ nhóm Lumine đi bắt “Dê Dừa” để đổi lấy Hương Bất Tử.')
BAIZHU = dict(name='Baizhu', role='Chủ Nhà Thuốc Bubu', img='baizhu_icon.png', desc='Ông chủ nhà thuốc cùng con rắn biết nói Changsheng. Bán Hương Bất Tử giá 299 vạn Mora sau khi bắt tay với Childe.')
GANYU = dict(name='Ganyu', role='Thư ký Nguyệt Hải Đình', img='ganyu_icon.png', desc='Thư ký của toàn thể Thất Tinh, sứ giả đặc biệt của Ningguang. Tìm đến quán Ba Cốc Say Mèm để trao thư mời Lumine đến Quần Ngọc Các.')
# --- Chương I · Màn III (Liyue) ---
KEQING_C3 = dict(name='Keqing', role='“Ngọc Hành Tinh” của Thất Tinh Liyue', img='keqing_icon.png', desc='Gặp Lumine bên máy Guizhong ở Thiên Hoành Sơn. Thẳng thắn, “bất kính với thần tiên”, tin rằng thời đại của tiên nhân đã qua.')
NINGGUANG_C3 = dict(name='Ningguang', role='“Thiên Quyền” của Thất Tinh Liyue', img='ningguang_icon.png', desc='Mời Lumine lên Quần Ngọc Các, chỉ cho cô dấu vết nghiên cứu Bách Vô Cấm Kỵ Lục của Fatui. Từ bỏ Quần Ngọc Các để trấn áp Ma Thần.')
GANYU_C3 = dict(name='Ganyu', role='Thư ký Nguyệt Hải Đình', img='ganyu_icon.png', desc='Sứ giả của Thiên Quyền Tinh, con lai giữa loài người và Kỳ Lân. Tặng Bách Hợp Lưu Ly cho Điển Lễ Tiễn Tiên.')
ZHONGLI_C3 = dict(name='Zhongli', role='Khách của Vãng Sinh Đường', img='zhongli_icon.png', desc='Cùng Lumine đi chặng cuối chuẩn bị Điển Lễ Tiễn Tiên, hiểu biết sâu rộng về lịch sử Liyue.')
CHILDE_C3 = dict(name='Childe', role='Quan Chấp Hành Fatui', img='childe_icon.png', desc='Tìm đến Hoàng Kim Ốc để đoạt Gnosis, giao chiến với Lumine, rồi dùng Bách Vô Cấm Kỵ Lục đánh thức Ma Thần Osial.')
SIGNORA_C3 = dict(name='Signora', role='Quan Chấp Hành thứ 8 của Fatui', img='signora_icon.png', desc='Kẻ từng cướp Gnosis của Phong Thần ở Mondstadt, xuất hiện trở lại ở Ngân Hàng Bắc Quốc tại Liyue.')
XIAO_C3 = dict(name='Xiao', role='Hộ Pháp Dạ Xoa · Hàng Ma Đại Thánh', img='xiao_icon.png', desc='Cùng các tiên nhân lên Quần Ngọc Các chống lại Ma Thần Lốc Xoáy.')
ADEPTI_C3 = dict(name='Ba vị Chân Quân', role='Tiên nhân Tuyệt Vân Gián', desc='Tước Nguyệt Trúc Dương, Lưu Vân Tá Phong và Lí Thủy Điệp Sơn Chân Quân đến Liyue hỏi tội Thất Tinh, rồi cùng Thất Tinh chống lại Ma Thần.')
PING_C3 = dict(name='Bình Lão Lão', role='Tiên nhân', desc='Lên tiếng bênh vực Ningguang và khuyên các tiên nhân hãy nhìn vào con người Liyue.')
OSIAL = dict(name='Osial', role='Ma Thần Lốc Xoáy', img='osial.png', desc='Ma Thần thất bại dưới tay Morax trong chiến tranh ma thần, bị trấn áp dưới Cô Vân Các, bị Childe đánh thức.')
MENGDAN = dict(name='Meng Dan', role='Người cung cấp hàng cho Minh Tinh Trai', desc='Bị Đạo Bảo Đoàn nhốt trong di tích, được Lumine cứu và tặng hộp đựng quà.')
# --- Màn III.1 (Razor) ---
RAZOR41 = dict(name='Razor', role='Thiếu niên được bầy sói nuôi lớn', img='razor_icon.png', desc='Sống cùng “Lupical” — bầy sói ở Lang Lãnh. Bị dân làng nghi là kẻ đứng sau vụ sói tập kích Thanh Tuyền Trấn.')
AMBER41 = dict(name='Amber', role='Kỵ Sĩ Trinh Thám · Đội Kỵ Sĩ Tây Phong', img='amber_icon.png', desc='Điều tra vụ đàn sói tập kích đội xe và Thanh Tuyền Trấn. Razor không nhớ tên cô, chỉ gọi là “cô gái màu đỏ”.')
BOREAS41 = dict(name='Vua Sói Bắc Phong', role='Lãnh chúa của Lang Lãnh · Boreas', img='boreas_icon.png', desc='“Ngài ấy” mà Razor nhắc đến. Người đặt ra cái tên “Lupical”.')
VILLAGERS41 = dict(name='Hopkins Thần Kỳ và Jotun', role='Dân Thanh Tuyền Trấn', desc='Muốn tự tay trả thù đàn sói sau vụ tập kích, gọi Razor là “người được sói nuôi lớn”.')
DRAFF = dict(name='Draff và Siegfria', role='Thợ săn ở Thanh Tuyền Trấn · Người đánh xe', desc='Draff lo cho những người trẻ dễ tức giận; Siegfria kể lại vụ đàn sói tập kích thị trấn.')

# --- Màn III.2 (Amber) ---
AMBER42 = dict(name='Amber', role='Kỵ Sĩ Trinh Thám · Quán Quân Bay Lượn', img='amber_icon.png', desc='Làm giám khảo kỳ thi bằng bay lượn của Lumine. Cầm nhầm quyển truyện ngụ ngôn về con chim nhỏ học bay thay cho sách hướng dẫn.')
OTTO = dict(name='Otto', role='Kỵ sĩ Đội Kỵ Sĩ Tây Phong', desc='Chặn Lumine lại để kiểm tra bằng bay lượn, kể về tên trộm “Quái Điểu” vừa đem văn vật của giáo đường trốn mất.')
RAPTOR = dict(name='Quái Điểu', role='Tội phạm của Thành Mondstadt', desc='Thường dùng Phong Chi Dực để gây án. Đội Kỵ Sĩ chưa đuổi kịp hắn lần nào.')
FARRAH = dict(name='Farrah', role='Thương nhân trái cây', desc='Đội xe bị Hilichurl tập kích sau khi một “quái nhân” từ trên trời rơi trúng doanh trại của chúng.')


# --- Chương II · Mở Đầu (Inazuma) ---
ATSUKO = dict(name='Atsuko', role='Người Inazuma sống ở cảng Liyue', desc='Người đã trốn khỏi Inazuma bằng chiếc bè nhỏ và được người Liyue cứu. Kể cho Lumine nghe về lệnh đóng cửa và chỉ cô đến tìm đội thuyền Nam Thập Tự.')
BEIDOU = dict(name='Beidou', role='Thủ lĩnh đội thuyền Nam Thập Tự', img='beidou_icon.png', desc='Chị đại hào sảng của chiếc thuyền “Ngôi Sao Chết Chóc”. Mời Lumine dự “Hội Đấu Võ Nam Thập Tự” và hứa tấm vé đến Inazuma cho người thắng.')
KAZUHA = dict(name='Kaedehara Kazuha', role='Ronin Samurai đến từ Inazuma', img='kazuha_icon.png', desc='Samurai phiêu bạt, nghe được “hơi thở” của gió và lá. Cung cấp chiếc Vision vô chủ làm giải thưởng và nhận ra Lumine dùng được nguyên tố mà không có Vision.')
ZHUHAN = dict(name='Zhuhan', role='Thuyền viên phụ trách báo danh', desc='Người ghi danh các tuyển thủ của Hội Đấu Võ và dẫn Lumine vào đấu trường qua từng vòng.')
CHUYUN = dict(name='Chú Yun', role='Tuyển thủ Hội Đấu Võ', desc='Á quân “Giải Đấu Võ Tự Do Ngật Hổ Nham”, kể về lần tay không bắt hai tên Đạo Bảo Đoàn.')
LINHSON = dict(name='Chai Yi và Liang', role='Truyền nhân “Phái Linh Sơn”', desc='Hai người trẻ luyện “Hóa Kình” và mong có Vision để làm sư phụ hài lòng.')
JINYOU = dict(name='Jinyou', role='Tuyển thủ tự nhận là “người hoàn hảo”', desc='Đối thủ đầu tiên của Lumine ở vòng dự tuyển.')
RONGSHI = dict(name='Rongshi', role='Đối thủ vòng bán kết', desc='Võ sĩ không muốn Vision, chỉ muốn tỷ võ để trưởng thành.')
FEI = dict(name='Fei', role='Đạo Bảo Đoàn, đối thủ chung kết', desc='Kẻ đã trộm chiếc Vision vô chủ nên không xuất hiện ở trận chung kết.')


SERIES = 'Genshin Impact · Light Novel'
FOOT = 'Truyện chuyển thể phi thương mại từ cốt truyện Genshin Impact (HoYoverse). Lời thoại theo bản tiếng Việt chính thức của game.'

# --- Chương II · Màn I (Inazuma) ---
BEIDOU_C2 = dict(name='Beidou', role='Thủ lĩnh đội thuyền Nam Thập Tự', img='beidou_icon.png', desc='Giữ lời hứa, đưa Lumine vượt qua giông bão đến Đảo Ritou trên thuyền “Ngôi Sao Chết Chóc”, rồi giao cô cho Thoma.')
THOMA = dict(name='Thoma', role='Người hầu của nhà Kamisato · Hiệp Hội Yashiro', img='thoma_icon.png', desc='Người đón Lumine ở Đảo Ritou, được Beidou giới thiệu là “thổ địa” và đối tác làm ăn. Bày ra những “khảo nghiệm” để xem cô có đủ sức “thay đổi thời cuộc” hay không.')
AYAKA = dict(name='Kamisato Ayaka', role='“Shirasagi Himegimi” · Đại tiểu thư Hiệp Hội Yashiro', img='ayaka_icon.png', desc='Người chống lại lệnh Truy Lùng Vision. Hứa tiến cử Lumine với Raiden Shogun nếu cô giúp ba người mất Vision.')
YOIMIYA = dict(name='Yoimiya', role='Chủ Tiệm Pháo Hoa Naganohara', img='yoimiya_icon.png', desc='“Nữ Hoàng Lễ Hội Hè” của Hanamizaka. Dùng Vision giả che mắt samurai và cùng Lumine lẻn vào Sở Trị An cứu sư phụ Masakatsu.')
SARA = dict(name='Kujou Sara', role='Đại tướng Quân Shogunate · Hiệp Hội Tenryou', img='sara_icon.png', desc='Con nuôi nhà Kujou, người thi hành lệnh Truy Lùng Vision. Trách phạt thuộc hạ dụng tư hình và tha cho nhóm Lumine đưa Masakatsu đi “chỉ lần này”.')
YAE = dict(name='Yae Miko', role='Đại pháp sư Đền Narukami', img='yae_icon.png', desc='“Yae đại nhân” có quan hệ thân thiết với Shogun. Chỉ ra căn bệnh của Domon và nói với Lumine rằng cô đến đúng thời cơ.')
CHISATO = dict(name='Hiiragi Chisato', role='Đại tiểu thư nhà Hiiragi · Hiệp Hội Kanjou', img='chisato_icon.png', desc='Nhờ Lumine đưa thư cho người thương Kujou Kamaji, đổi lại giúp cô trốn khỏi Đảo Ritou bằng đoàn hàng đi Đảo Watatsumi.')
SHINSUKE = dict(name='Hiiragi Shinsuke', role='Gia chủ nhà Hiiragi · Hiệp Hội Kanjou', desc='Tiếp đón Lumine niềm nở nhưng giao những việc vô lý để giữ chân cô lại Đảo Ritou.')
WERNER = dict(name='Werner', role='Thương nhân người Mondstadt kẹt ở Đảo Ritou', desc='Kẻ bán “Tủy Pha Lê” giá cao cho Keijirou. Nhớ quê, cuối cùng khai ra mưu đồ và dẫn Lumine đi tìm bằng chứng.')
KURISU = dict(name='Kurisu', role='Hội trưởng Thương Hội Vạn Quốc', desc='Thương nhân người Fontaine, bạn thân của Thoma, đang khốn đốn vì thuế “Tủy Pha Lê”.')
TEJIMA = dict(name='Tejima', role='Người canh giữ Làng Konda', img='tejima_icon.png', desc='Bảo vệ làng suốt 30 năm để chờ một người. Mất Vision và quên đi lý do mình ở lại.')
KUROSAWA = dict(name='Kurosawa Kyounosuke', role='Samurai Quân Shogunate', img='kurosawa_icon.png', desc='Tự bỏ tiền mua “lương thực cứu tế” cho dân, sau khi mất Vision thì quên hết và bị dân làng trách móc.')
DOMON = dict(name='Domon', role='Chưởng môn phái Meikyou Shisui', desc='Kiếm đạo gia muốn thành thiên hạ đệ nhất, phát điên sau khi mất Vision. Được sư huynh Anzai và các đệ tử giúp tỉnh lại.')
MASAKATSU = dict(name='Masakatsu', role='Nghệ nhân làm Vision giả', desc='Người làm Vision giả giúp Hiệp Hội Yashiro, bị Hiệp Hội Tenryou bắt giam ở Sở Trị An.')

# Chương II · Màn III
KOKOMI3 = dict(name='Sangonomiya Kokomi', role='Người Trị Vì Đảo Watatsumi · Thống soái quân kháng chiến', img='kokomi_icon.png', desc='Phong Lumine làm đội trưởng “Đội Cá Kiếm 2”. Khi phát hiện “vũ khí bí mật” của nhà tài trợ là Delusion của Fatui, cô ra lệnh tịch thu toàn bộ và chỉ cho Lumine nơi có thể là công xưởng.')
TEPPEI3 = dict(name='Teppei', role='Đội trưởng “Đội Cá Trích 1” · Quân kháng chiến', img='teppei_icon.png', desc='Người bạn đưa Lumine về Đảo Watatsumi. Lập nhiều chiến công nhờ “vũ khí bí mật” của nhà tài trợ, mà không biết đó là Delusion đang hút cạn sinh mạng mình.')
GOROU3 = dict(name='Gorou', role='Đại tướng quân kháng chiến', img='gorou_icon.png', desc='Phát hiện quân sĩ lão hóa kỳ lạ vì lén dùng “vũ khí bí mật”, mang một chiếc đến cho Kokomi. Dẫn quân kháng chiến xông lên trong trận chiến cuối cùng.')
OOKUBO = dict(name='Ookubo Daisuke', role='Quân kháng chiến · Đảo Watatsumi', desc='Người bàn chuyện quân lương với Kokomi, kể về nhà tài trợ giấu mặt.')
KOUTOKU = dict(name='Koutoku và Yoshihisa', role='Đội Cá Kiếm 2', desc='Đội trưởng đại diện và thành viên lão làng của Đội Cá Kiếm 2. Thử thách Lumine bằng đám ronin rồi công nhận cô làm đội trưởng.')
SCARA = dict(name='Scaramouche', role='Quan Chấp Hành thứ 6 của Fatui', img='scaramouche_icon.png', desc='Người “thay mặt thực hiện kế hoạch” ở công xưởng Delusion trên Đảo Yashiori. Khiêu khích Lumine bằng cái chết của Teppei và dùng oán niệm Ma Thần giăng bẫy cô.')
YAE3 = dict(name='Yae Miko', role='Guuji Đền Narukami · “Gia quyến” của Lôi Thần', img='yae_icon.png', desc='Cứu Lumine khỏi tay Scaramouche, kể về Ei và “Nhất Tâm Tịnh Thổ”, rồi vạch kế hoạch ly gián Hiệp Hội Tenryou để đưa Lumine trở lại trước mặt Raiden Shogun.')
SARA3 = dict(name='Kujou Sara', role='Đại tướng Quân Shogunate · Hiệp Hội Tenryou', img='sara_icon.png', desc='Đòi bắt Lumine ở Đền Narukami, nhận lời hẹn ba ngày của Yae Miko. Khi thấy chứng cứ, cô đối chất với gia chủ Kujou Takayuki và quyết định kháng lệnh.')
SAYU = dict(name='Sayu', role='Ninja của Shuumatsuban', img='sayu_icon.png', desc='Ninja hay buồn ngủ được Yae Miko “tóm” đến giúp. Lẻn vào Hiệp Hội Tenryou lấy công văn và thư từ trao đổi với Fatui.')
THOMA3 = dict(name='Thoma', role='Người hầu của nhà Kamisato · Hiệp Hội Yashiro', img='thoma_icon.png', desc='Vẫn trốn trong Phòng Trà Komore, nghĩ ra kế dùng pháo hoa của Yoimiya để dụ thân binh Hiệp Hội Tenryou.')
AYAKA3 = dict(name='Kamisato Ayaka', role='Đại tiểu thư nhà Kamisato', img='ayaka_icon.png', desc='Nhận ra công văn của Hiệp Hội Tenryou trình lên Shogun có vấn đề, cùng Lumine lập kế hoạch lấy chứng cứ.')
YOIMIYA3 = dict(name='Yoimiya', role='Chủ Tiệm Pháo Hoa Naganohara', img='yoimiya_icon.png', desc='Tặng Lumine một loại pháo hoa “siêu to khổng lồ” để dụ lính gác.')
TAKAYUKI = dict(name='Kujou Takayuki', role='Gia chủ nhà Kujou · Hiệp Hội Tenryou', img='takayuki_icon.png', desc='Thừa nhận đã qua lại với Fatui và che giấu chuyện tiền tuyến trong công văn trình lên Shogun, vì tin vào sức mạnh của “Lưỡi Đao Vô Tưởng”.')
SIGNORA3 = dict(name='Signora', role='Quan Chấp Hành thứ 8 của Fatui · Sứ giả Snezhnaya', img='signora_icon.png', desc='Kẻ giật dây chiến loạn ở Inazuma. Bị Lumine thách “Ngự Tiền Quyết Đấu” ở Thiên Thủ Các và thua trận.')
RAIDEN3 = dict(name='Raiden Shogun', role='Lôi Thần · Ei', img='raiden_icon.png', desc='Chứng kiến cuộc quyết đấu ở Thiên Thủ Các. Trong “Nhất Tâm Tịnh Thổ”, Ei bị nguyện vọng của người dân và Lumine đánh bại, rồi phế bỏ Lệnh Truy Lùng Vision.')
KAZUHA3 = dict(name='Kaedehara Kazuha', role='Ronin Samurai', img='kazuha_icon.png', desc='Xuất hiện trong trận chiến cuối cùng, đỡ lấy nhát “Lưỡi Đao Vô Tưởng”.')


# Mỗi màn: id (dùng làm tên thư mục web), arc (phần truyện), file nguồn, nhãn, tên, phụ đề, ảnh bìa, nhân vật, tên PDF, chân trang PDF, side=True nếu là nhiệm vụ bắt buộc (Màn X.1)
# --- Chương II · Màn I.1 (Kamisato Ayaka), Màn I.2 (Yoimiya), Màn II ---
AYAKA11 = dict(name='Kamisato Ayaka', role='“Shirasagi Himegimi” · Đại tiểu thư Hiệp Hội Yashiro', img='ayaka_icon.png', desc='Nhờ Lumine cùng chuẩn bị quà gặp mặt cho “Tsubaki”, cái tên lặp đi lặp lại trong sổ tay của người mẹ đã mất.')
OGURA = dict(name='Ogura Mio', role='Chủ Tiệm Vải Ogura', desc='Nhận may bộ kimono theo bản thiết kế của Ayaka, nhưng thiếu vải hoa nghê thường nhập từ Liyue.')
KURISU11 = dict(name='Kurisu', role='Hội trưởng Thương Hội Vạn Quốc', desc='Bị đám Ronin cướp mất lô vải cao cấp. Được Ayaka giúp lấy lại hàng.')
RONIN11 = dict(name='Ronin', role='Kẻ cướp hàng', desc='Cướp hàng của Thương Hội Vạn Quốc rồi đòi Kurisu bỏ tiền chuộc lại.')
KIMINAMI = dict(name='Kiminami Anna', role='Chủ Nhà Hàng Kiminami', desc='Quen biết anh em nhà Kamisato đã lâu, vui mừng khi thấy Ayaka dẫn bạn đến quán.')
FESTIVAL = dict(name='Sanden, Shimizu, Murakami, Yoshikawa', role='Chủ các sạp hàng ở lễ hội', desc='Nhiệt tình đón Ayaka đến lễ hội: tặng mặt nạ, mời rút quẻ, cho công thức bánh và bán thẻ cầu nguyện.')
YOIMIYA12 = dict(name='Yoimiya', role='Chủ Tiệm Pháo Hoa Naganohara', img='yoimiya_icon.png', desc='Bận rộn chuẩn bị “Hội Pháo Hoa Naganohara”, đồng thời tìm cách giúp kẻ vượt biên Sakujirou.')
KIDS12 = dict(name='Matsuzaka, Saika, Iwao', role='Lũ trẻ ở Đảo Narukami', desc='Muốn đánh đuổi “Siêu Mujina Youkai” bằng “vũ khí” chị Yoimiya chuẩn bị.')
RYUUNOSUKE = dict(name='Naganohara Ryuunosuke', role='Cha của Yoimiya', desc='Chủ cũ của Tiệm Pháo Hoa Naganohara, tai không còn nghe rõ nhưng luôn tươi cười và thích kể chuyện.')
SAKUJIROU = dict(name='Sakujirou', role='Kẻ vượt biên', desc='Người Inazuma đã bỏ đi, nay lén trở về và trốn trong Tiệm Pháo Hoa Naganohara.')
KOUICHI = dict(name='Kouichi', role='Bạn của Yoimiya', desc='Lén đóng thuyền để Sakujirou có đường rời Inazuma.')
MORIHIKO = dict(name='Morihiko', role='Khách quen của tiệm pháo hoa', desc='Chuẩn bị sẵn khoáng thạch làm pháo hoa cho Yoimiya.')
AMENOMA = dict(name='Amenoma Tougo và Hajime', role='Xưởng Rèn Amenoma', desc='Hai thầy trò thợ rèn. Amenoma Tougo đích thân gia công khoáng thạch cho Yoimiya.')
IMATANI = dict(name='Imatani Saburou và Imatani Kaori', role='Đôi vợ chồng già, khách cũ của tiệm pháo hoa', desc='Cha mẹ của Imatani Keisuke, sắp kỷ niệm 50 năm bên nhau.')
SATORU = dict(name='Satoru', role='Người dân Làng Konda', desc='Nhận Củ Cải Mặn do bà Kaori gửi đến.')
KEISUKE = dict(name='Imatani Keisuke', role='Hiệp Hội Tenryou', desc='Bạn thân thuở nhỏ của Sakujirou, nay là người dẫn quân truy bắt anh.')
YOSHITAKA = dict(name='Yoshitaka', role='Lính Hiệp Hội Tenryou', desc='Thuộc hạ của Keisuke, chặn đường nhóm Yoimiya.')
AYAKA2 = dict(name='Kamisato Ayaka', role='“Shirasagi Himegimi” · Đại tiểu thư Hiệp Hội Yashiro', img='ayaka_icon.png', desc='Báo tin Thoma bị Hiệp Hội Tenryou bắt đi làm “Vision thứ 100”.')
THOMA2 = dict(name='Thoma', role='Người hầu của nhà Kamisato · Hiệp Hội Yashiro', img='thoma_icon.png', desc='Bị bắt trong Nghi Thức Săn Vision. Cứu Lumine khỏi tay Raiden Shogun rồi chỉ cô đến Tatarasuna.')
RAIDEN = dict(name='Raiden Shogun', role='Vị thần cai trị Inazuma', img='raiden_icon.png', desc='Gọi Lumine là “ngoại lệ”, kẻ thù của sự vĩnh hằng, và đánh gục cô trong Nghi Thức Săn Vision.')
TEPPEI = dict(name='Teppei', role='Lính quân kháng chiến', img='teppei_icon.png', desc='Được Lumine cứu ở tiền tuyến, tiến cử cô với Gorou và dẫn cô đi khắp doanh trại.')
GOROU = dict(name='Gorou', role='Đại tướng quân kháng chiến', img='gorou_icon.png', desc='Thống lĩnh quân kháng chiến ở Tatarasuna. Nhận Lumine vào quân và không chịu giao cô cho Kujou Sara.')
SARA2 = dict(name='Kujou Sara', role='Đại tướng Quân Shogunate · Hiệp Hội Tenryou', img='sara_icon.png', desc='Dẫn viện binh đến tiền tuyến, đòi Gorou giao nộp Lumine và đề nghị “lâm trận quyết đấu”.')
KOKOMI = dict(name='Sangonomiya Kokomi', role='Thánh Pháp Sư của Đảo Watatsumi', img='kokomi_icon.png', desc='Người tổ chức quân kháng chiến. Đến Bờ Nazuchi cùng đội thuyền Nam Thập Tự, đẩy lui Quân Shogunate.')
KAZUHA2 = dict(name='Kaedehara Kazuha', role='Ronin Samurai · đội thuyền Nam Thập Tự', img='kazuha_icon.png', desc='Xuất hiện cùng Kokomi và đội thuyền Nam Thập Tự giữa trận chiến ở Bờ Nazuchi.')
BEIDOU2 = dict(name='Beidou', role='Thủ lĩnh đội thuyền Nam Thập Tự', img='beidou_icon.png', desc='Đưa “Ngôi Sao Chết Chóc” phục kích Quân Shogunate để hỗ trợ quân kháng chiến.')
RESIST = dict(name='Kaida Ryouma, Tokuda, Masashi, Shouji, Hisahiko', role='Người của quân kháng chiến', desc='Những người lính, thương binh và tân binh mà Lumine gặp trong doanh trại ở Tatarasuna.')

# --- Chương Đệm · Màn I ---
SHENHE = dict(name='Shenhe', role='Đệ tử của Lưu Vân Tá Phong Chân Quân', img='shenhe_icon.png', desc='Cô gái tóc trắng được Lumine giúp thoát khỏi đám lừa đảo ở Cảng Liyue. Lớn lên cùng tiên nhân nhưng là người phàm, mang Bùa Chú Tiên Gia đến cho Ningguang và giúp Lumine trong cuộc thi trùng tu Quần Ngọc Các.')
YUNJIN = dict(name='Yun Jin', role='Diễn viên nhạc kịch nổi tiếng của Liyue', img='yunjin_icon.png', desc='Đến tham gia cuộc thi để hỏi Ningguang về sân khấu cho vở kịch “Thần Nữ Hủy Diệt” của cha mình. Đề nghị nhóm Lumine và Beidou lập đội cùng giành ba suất đầu.')
XINGQIU = dict(name='Xingqiu', role='Nhị thiếu gia Thương Hội Phi Vân', img='xingqiu_icon.png', desc='Chỉ cho nhóm Lumine động tiên của Minh Hải Thê Hà Chân Quân ở gần Ngoại Ô Li Sa, nơi có thể có Minh Hà Phù Sinh Thạch.')
NINGGUANG_CD = dict(name='Ningguang', role='“Thiên Quyền” của Thất Tinh Liyue', img='ningguang_icon.png', desc='Tổ chức cuộc thi tìm nguyên liệu để trùng tu Quần Ngọc Các, đồng thời dùng việc này để dụ Beisht, kẻ đi theo Ma Thần Lốc Xoáy, ra khỏi mặt biển.')
BEIDOU_CD = dict(name='Beidou', role='Thủ lĩnh đội thuyền Nam Thập Tự', img='beidou_icon.png', desc='Mang đến một khối Minh Hà Phù Sinh Thạch, cùng Lumine và Yun Jin giành ba suất đầu của cuộc thi. Là người đã cảnh báo Ningguang về biến động dưới biển.')
CLOUD_CD = dict(name='Lưu Vân Tá Phong Chân Quân', role='Sư phụ của Shenhe', img='cloudretainer.png', desc='Kể cho Lumine và Paimon nghe quá khứ của Shenhe, nhờ họ chăm sóc con bé, và âm thầm quan sát xem Ningguang có vượt qua được phong ba sắp tới không.')
BAIZHU_CD = dict(name='Baizhu', role='Chủ Nhà Thuốc Bubu', img='baizhu_icon.png', desc='Cho nhóm Lumine biết về Minh Hà Phù Sinh Thạch trong “Thất Tàng Sơn Kinh” và gợi ý đến Thương Hội Phi Vân hỏi thăm.')
KEQING_CD = dict(name='Keqing', role='“Ngọc Hành Tinh” của Thất Tinh Liyue', img='keqing_icon.png', desc='Chỉ huy Thiên Nham Quân, ra lệnh cho máy Guizhong kiểu mới khai hỏa vào Beisht.')
BAIWEN = dict(name='Baiwen', role='Thư ký của Ningguang ở công trường', img='baiwen_icon.png', desc='Người nhận và chấm nguyên liệu của cuộc thi trùng tu Quần Ngọc Các.')
ZHANG = dict(name='Lão Zhang', role='Thợ rèn tiệm Hàn Phong Thiết Khí', img='zhang_icon.png', desc='Người từng làm Lõi Thần Kỳ cho Ningguang, chỉ cho nhóm Lumine đi tìm Quặng Sắt Sao Vỡ và Bí Hoa Thạch.')
MINGJUN = dict(name='Mingjun', role='Bạn thân của cha Shenhe', img='mingjun_icon.png', desc='Ông lão ở ngôi làng bỏ hoang gần Thiên Hoành Sơn, nơi Shenhe sinh ra. Nhiều năm vẫn day dứt vì đã không ngăn được cha của Shenhe.')
BEISHT = dict(name='Beisht', role='“Tàn Dư Lốc Xoáy”', img='beisht_icon.png', desc='Vợ của Osial, người cuối cùng đi theo Ma Thần Lốc Xoáy. Trồi lên từ biển khi Quần Ngọc Các bay lên.')
LIU = dict(name='Liu Mặt Sẹo và Qiang', role='Kẻ bán tình báo', desc='Hai gã lưu manh bám theo Shenhe đòi tiền, bị Thiên Nham Quân bắt đi.')

# --- Chương II · Màn IV ---
KATHERYNE_C2M4 = dict(name='Katheryne', role='Hiệp Hội Nhà Mạo Hiểm', desc='Giới thiệu cho Lumine ủy thác của người thợ mỏ Yuehui ở Vực Đá Sâu. Sáng hôm đó cô rút quẻ được lời dự báo về một “cuộc hội ngộ bất ngờ”.')
YUEHUI = dict(name='Yuehui', role='Thợ mỏ ở Vực Đá Sâu', img='yuehui_icon.png', desc='Một trong những thợ mỏ đầu tiên được cấp giấy phép khai thác Vực Đá Sâu. Ủy thác Lumine điều tra những Hilichurl chạy vào Vực Đá Sâu rồi không quay trở ra.')
DAIN_C2M4 = dict(name='Dainsleif', role='“Kiếm Sĩ Hoàng Hôn” · cựu đội trưởng đội cận vệ hoàng gia Khaenri\'ah', img='dainsleif_icon.png', desc='Đuổi theo một Sứ Đồ Vực Sâu qua cổng dịch chuyển và lạc đến Vực Đá Sâu, gặp lại Lumine. Cùng cô điều tra tòa thành đảo ngược, nơi có khả năng làm suy yếu lời nguyền.')
HALFDAN = dict(name='Halfdan', role='Kỵ Sĩ Hắc Xà', img='halfdan_icon.png', desc='Tinh anh trẻ tuổi trong đội cận vệ hoàng gia Khaenri\'ah năm xưa. Vẫn giữ được ý chí sau năm trăm năm, dẫn các Kỵ Sĩ Hắc Xà bảo vệ những Hilichurl đang chờ kết cục của mình.')
AETHER_C2M4 = dict(name='Aether', role='Anh trai song sinh của Lumine · “Hoàng tử điện hạ”', img='aether_icon.png', desc='Hiện ra trong ký ức mà Lumine thấy khi chạm vào hoa Inteyvat, đồng ý để Sứ Đồ Vực Sâu dùng “thiết bị” thanh tẩy lời nguyền.')
HERALD_C2M4 = dict(name='Sứ Đồ Vực Sâu', img='herald_icon.png', role='Giáo Đoàn Vực Sâu', desc='Kẻ từng bỏ chạy khỏi Dainsleif qua cổng dịch chuyển. Chặn đường nhóm Lumine để bảo vệ “ý chí của điện hạ” và bị đánh bại.')
LECTOR = dict(name='Linh Mục Vực Sâu', role='Giáo Đoàn Vực Sâu', desc='Canh giữ thiết bị khuếch đại ở căn phòng trung tâm của di tích, bị Lumine đánh bại.')
BSK = dict(name='Kỵ Sĩ Hắc Xà', role='Cựu cận vệ hoàng gia Khaenri\'ah', desc='Những kỵ sĩ mang lời nguyền canh giữ di tích và những Hilichurl già yếu. Theo Dainsleif, họ đang hô “mau chạy đi” bằng tiếng Khaenri\'ah cổ.')

# --- Chương Đệm · Màn I.1 (nhiệm vụ thế giới Vực Đá Sâu) ---
MUNING = dict(name='Muning', role='Chuyên viên Tổng Vụ ở Vực Đá Sâu', img='muning_icon.png', desc='Phụ trách doanh trại ở lối vào Vực Đá Sâu, cấp giấy phép cho những người muốn xuống hầm mỏ. Tính tình nóng nảy nhưng không phải người xấu.')
ZHIQIONG = dict(name='Zhiqiong', role='Nhà mạo hiểm · người thăm dò của đội thăm dò', img='zhiqiong_icon.png', desc='Nhà mạo hiểm trẻ hâm mộ Lumine, gọi cô là “tiền bối”. Chịu trách nhiệm tìm đường và vẽ bản đồ cho đội thăm dò Vực Đá Sâu.')
JINWU = dict(name='Jinwu', role='Kỹ thuật viên an ninh của đội thăm dò', img='jinwu_icon.png', desc='Sửa chữa và bảo trì thiết bị, đảm bảo an toàn cho cả đội. Luôn để mắt đến Zhiqiong.')
KHEDIVE = dict(name='Khedive', role='Học giả đến từ Sumeru', img='khedive_icon.png', desc='Người bỏ tiền thành lập và phụ trách đội thăm dò, nghiên cứu khoáng sản và sinh vật học.')
CLITOPHO = dict(name='Clitopho', role='Người bán “Thuốc Hảo Hán”', img='clitopho_icon.png', desc='Từng theo Đạo Bảo Đoàn, được Lumine cứu khỏi lồng giam rồi gia nhập đội thăm dò, giúp chế tạo đạn pháo.')

# --- Chương Đệm · Màn II ---
YELAN = dict(name='Yelan', role='Người tự xưng làm việc ở Tổng Vụ', img='yelan_icon.png', desc='Giám sát Vực Đá Sâu. Bí ẩn, quan sát tinh tường, đang điều tra chân tướng trận chiến với ma thú Khaenri\'ah năm trăm năm trước.')
YANFEI = dict(name='Yanfei', role='Cố vấn pháp lý nổi tiếng của Liyue', img='yanfei_icon.png', desc='Mang huyết thống tiên thú. Đến Vực Đá Sâu để thực hiện một bản di chúc: tìm lại pháp bảo La Bàn Huyền Ảo.')
ITTO = dict(name='Arataki Itto', role='Đại ca Bang Arataki', img='itto_icon.png', desc='Người Inazuma đến Liyue cùng Shinobu. Được Yanfei giúp thoát khỏi đại lao Liyue, nên bám theo để “báo ơn”.')
SHINOBU = dict(name='Kuki Shinobu', role='Thành viên Bang Arataki', img='shinobu_icon.png', desc='Người lo liệu mọi việc trong Bang Arataki. Từng học luật ở Liyue, đến lấy bằng tốt nghiệp.')
USHI = dict(name='Ushi', role='Thành viên ngoài biên chế của Bang Arataki', desc='Chú bò của Itto, giỏi tìm đường. Chỉ nói “Moo”, nhưng Itto hiểu hết.')
XIAO_CD2 = dict(name='Xiao', role='Hộ Pháp Dạ Xoa · Hàng Ma Đại Thánh', img='xiao_icon.png', desc='Một mình đến Vực Đá Sâu tìm tung tích của một Dạ Xoa đã mất tích.')
FUSHE = dict(name='Phù Xá', role='Đằng Xà Thái Nguyên Soái · Dạ Xoa', img='bosacius_icon.png', desc='Người đứng đầu trong năm Dạ Xoa dưới trướng Nham Vương Đế Quân, đã mất tích hàng trăm năm. Xiao đến Vực Đá Sâu để tìm anh.')
BOYANG = dict(name='Boyang', role='Thuật sĩ · tổ tiên của Yelan', desc='Một trong các tổ tiên của Yelan, người năm xưa đến Vực Đá Sâu và không thể trở về.')
ZHONGLI_CD2 = dict(name='Zhongli', role='Khách của Vãng Sinh Đường', img='zhongli_icon.png', desc='Lặng lẽ dõi theo từ trên vách núi.')

# --- Chương III · Màn I (Sumeru) ---
TIGHNARI = dict(name='Tighnari', role='Đội Trưởng Kiểm Lâm · Làng Gandharva', img='tighnari_icon.png', desc='Người thầy của Collei, am hiểu thực vật và bào chế thuốc. Đã nhiều lần từ chối lời mời nhậm chức của Giáo Viện, cùng Lumine đi giải quyết Tử Vực và tìm cách cứu Haypasia.')
COLLEI = dict(name='Collei', role='Kiểm lâm tập sự · Làng Gandharva', img='collei_icon.png', desc='Học trò của Tighnari, bạn thư từ của Amber ở Mondstadt. Đã đưa Lumine ngất xỉu về làng; từ nhỏ mắc bệnh Eleazar nên phải hạn chế chạm vào đồ vật.')
KIEMLAM = dict(name='Amir và Nasrin', role='Nhân viên kiểm lâm · Làng Gandharva', desc='Hai nhân viên kiểm lâm của làng, thường nói chuyện với Tighnari về việc tuần tra, nấm độc và Tử Vực.')
HAYPASIA = dict(name='Haypasia', role='Học giả Học Phái Rtawahist · Giáo Viện', img='haypasia_icon.png', desc='Học giả ẩn cư trong hang núi, dùng Linh Phân Hương để thiền định và kết nối với Cây Thế Giới. Lumine ngất đi vì làn khói hương của cô.')
HERALD_C3 = dict(name='Sứ Đồ Vực Sâu', role='Giáo Đoàn Vực Sâu', img='herald_icon.png', desc='Xuất hiện trong giấc mơ của Lumine ở hang núi, nói rằng “Hoàng tử đại nhân” đã bỏ rơi cô và hành trình tìm anh vốn đã không còn ý nghĩa.')
GIAOVIEN = dict(name='Ghulam và Khajeh', role='Người của Giáo Viện', desc='Hai người của Giáo Viện đến Làng Gandharva để mời Tighnari về Thành Sumeru, bị Tighnari từ chối.')
PANAH = dict(name='Panah, Rohawi và Asfand', role='Giáo Viện · Lữ Đoàn 30', desc='Panah trao Trạm Cuối Akasha cho khách mới đến Thành Sumeru, Rohawi là nhà nghiên cứu quen biết Tighnari, Asfand là cố vấn của Lữ Đoàn 30, nhóm Eremite phụ trách an ninh thành.')
DUNYARZAD = dict(name='Dunyarzad', role='Tiểu thư nhà Homayani', img='dunyarzad_icon.png', desc='Tín đồ trung thành của Tiểu Vương Kusanali, đang chuẩn bị Lễ Hội Sabzeruz. Cho Lumine biết Tiểu Vương Kusanali thật sự được người dân yêu mến.')
DEHYA = dict(name='Dehya', role='Eremite · Vệ sĩ của Dunyarzad', img='dehya_icon.png', desc='Vệ sĩ của Dunyarzad, mạnh mẽ và thẳng tính, luôn theo sát tiểu thư để bảo vệ cô.')
NILOU = dict(name='Nilou', role='Vũ công · Đại Khu Bazaar', img='nilou_icon.png', desc='Vũ công đang cùng mọi người trang trí Đại Khu Bazaar và chuẩn bị điệu múa cho Lễ Hội Sabzeruz, mời Lumine đừng bỏ lỡ lễ hội.')
ALHAITHAM = dict(name='Alhaitham', role='Học giả · Giáo Viện', img='alhaitham_icon.png', desc='Học giả của Giáo Viện, muốn nghiên cứu “Hũ Tri Thức Thần”. Cùng Lumine truy tìm nó ở Cảng Ormos, rồi giao đấu với nhóm Ayn Al-Ahmar.')
DORI = dict(name='Dori', role='Thương nhân bách hóa · Cảng Ormos', img='dori_icon.png', desc='Thương nhân mê Mora ở Cảng Ormos, bán đủ thứ hàng và tình báo. Giúp Lumine tìm ra manh mối về Hũ Tri Thức Thần.')
AYN = dict(name='Tariq và Tumart', role='Nhóm Eremite Ayn Al-Ahmar', desc='Thành viên của Ayn Al-Ahmar, những người tôn thờ Vua Deshret và giữ trong tay “Hũ Tri Thức Thần”.')
GIAOVIEN2 = dict(name='Học sinh Giáo Viện và người dân Sumeru', role='Những người khác', desc='Các học sinh và người dân Thành Sumeru, Cảng Ormos gặp trên đường đi: Lambad, Muruwa, Hamasa, Sharaf, Aftab, Kumari, Shrimati, Farhad, Rama, Pooria, Jayant, Elham, Sidhu, Bandi, Kudari, Eymen, Latish, Raunak.')
KATHERYNE_C3 = dict(name='Katheryne', role='Hiệp Hội Nhà Mạo Hiểm · Thành Sumeru', desc='Nhân viên hiệp hội tại Thành Sumeru, cho Lumine biết thêm tình hình và chỉ đường.')

# --- Chương III · Màn II (Sumeru) ---
DUNYARZAD2 = dict(name='Dunyarzad', role='Tiểu thư nhà Homayani · người tổ chức Lễ Hội Sabzeruz', img='dunyarzad_icon.png', desc='Tiết lộ mình mắc bệnh Eleazar giai đoạn cuối, vẫn dốc sức tổ chức Lễ Hội Sabzeruz để mừng sinh nhật Tiểu Vương Kusanali, và là người cùng Lumine bị cuốn vào vòng “samsara”.')
DEHYA2 = dict(name='Dehya', role='Eremite · Vệ sĩ của Dunyarzad', img='dehya_icon.png', desc='Bảo vệ Dunyarzad và buổi lễ, cùng Lumine đối đầu Eremite định bắt cóc cô, rồi bị cuốn vào việc chứng minh “cọc gỗ” trong vòng lặp ngày lễ.')
NILOU2 = dict(name='Nilou', role='Vũ công · Đại Khu Bazaar', img='nilou_icon.png', desc='Chuẩn bị biểu diễn Vũ Điệu Sabzeruz, bị Giáo Viện cấm; cuối cùng điệu múa vẫn diễn ra với hai chậu Padisarah.')
NAHIDA = dict(name='Nahida', role='Cô gái bí ẩn', img='nahida_icon.png', desc='Cô gái nhỏ nhắn chỉ vài người nhìn thấy, tự xưng là “mặt trăng” và nhắc Lumine rằng họ đang bị nhốt trong một “samsara”. Cuối màn, Lumine nhận ra cô là Tiểu Vương Kusanali.')
KIMIYA = dict(name='Kimiya', role='Người bán “Bói Giả Kim”', img='kimiya_icon.png', desc='Bày quầy “Bói Giả Kim” trong lễ hội, dùng nguyên liệu của khách để luyện kim rồi đoán ý nghĩa từ kết quả.')
VIHAR = dict(name='Vihar', role='Người đóng “Kỵ Sĩ Hoa Farris”', img='vihar_icon.png', desc='Phát Kẹo Yalda cho trẻ em trong lễ hội, tự xưng “Kỵ Sĩ Hoa Farris” và rất quý Dunyarzad.')
AZAR = dict(name='Azar', role='Đại Hiền Giả · Giáo Viện', img='azar_icon.png', desc='Ra lệnh dỡ bỏ Vũ Điệu Sabzeruz và cấm lễ hội, cho rằng tự ý tổ chức lễ hội của thần là vi phạm lệnh cấm.')
SETARIA = dict(name='Setaria', role='Người của Giáo Viện', desc='Đi cùng Azar, đọc lệnh cấm tổ chức Lễ Hội Sabzeruz.')
BADIS = dict(name='Badis và Idder', role='Eremite', desc='Hai Eremite định bắt cóc Dunyarzad trong lễ hội.')
AMAL = dict(name='Amal và Lambad', role='Chủ quầy · Chủ quán rượu', desc='Amal bán “Bàn Tiệc Haft-Mewa” trong lễ hội, Lambad là chủ Quán Rượu Lambad.')
OTHERS_C32 = dict(name='Người dân Thành Sumeru', role='Những người khác', desc='Bọn trẻ trong lễ hội, vệ binh và thương nhân ở cổng thành, một người lạ xuất hiện ở cuối màn.')

ACTS = [
  dict(id='man1', arc='Mở Đầu', src='man1.txt', act='Mở Đầu · Màn I', title='Người Phương Xa Đuổi Theo Gió', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='traveler_portrait.png', cast=[LUMINE, PAIMON, AETHER, GOD, AMBER, KAEYA, JEAN, LISA, DRAGON, BOY, VOICE],
       pdf='GenshinLN_MoDau_Man1_NguoiPhuongXaDuoiTheoGio.pdf', footer='Mở Đầu · Màn I — Người Phương Xa Đuổi Theo Gió', side=False),
  dict(id='man1-1', arc='Mở Đầu', src='man1_1.txt', act='Mở Đầu · Màn I.1', title='Ba Ngôi Đền Của Tứ Phong', sub='Nhiệm vụ bắt buộc để hoàn thành Màn I — Amber, Kaeya, Lisa',
       hero='lisa_splash.png', cast=[LUMINE, PAIMON, AMBER, KAEYA, LISA, JEAN, REDHAIR, MAGE, DVALIN],
       pdf='GenshinLN_MoDau_Man1.1_BaNgoiDenTuPhong.pdf', footer='Mở Đầu · Màn I.1 — Ba Ngôi Đền Của Tứ Phong', side=True),
  dict(id='man2', arc='Mở Đầu', src='man2.txt', act='Mở Đầu · Màn II', title='Vì Một Ngày Mai Không Rơi Lệ', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='venti_splash.png', cast=[LUMINE, PAIMON, VENTI, JEAN, DILUC, LISA, DVALIN2, MAGE2, ANASTASIA, GOTELINDE, SIGNORA],
       pdf='', footer='Mở Đầu · Màn II — Vì Một Ngày Mai Không Rơi Lệ', side=False),
  dict(id='man3', arc='Mở Đầu', src='man3.txt', act='Mở Đầu · Màn III', title='Bài Ca Về Rồng Và Tự Do', sub='Nhiệm vụ Ma Thần — Mondstadt',
       hero='dvalin_wide.png', cast=[LUMINE, PAIMON, VENTI3, JEAN3, DILUC3, DVALIN3, MAGE3, AMBER3, KAEYA3, BARBARA, SIGNORA3],
       pdf='', footer='Mở Đầu · Màn III — Bài Ca Về Rồng Và Tự Do', side=False),
  dict(id='c1-man1', arc='Chương I · Liyue', src='c1_man1.txt', act='Chương I · Màn I', title='Phù Thế Phù Sinh Thiên Nham Gian', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='childe_card.png', cast=[LUMINE, PAIMON, CHILDE, NINGGUANG, REX, MOONCARVER, XIAO, GOLDET, YANXIAO, MING, MOUNTAIN, CLOUD, LIDING],
       pdf='', footer='Chương I · Màn I — Phù Thế Phù Sinh Thiên Nham Gian', side=False),
  dict(id='c1-man2', arc='Chương I · Liyue', src='c1_man2.txt', act='Chương I · Màn II', title='Lời Tạm Biệt Thể Xác Vĩnh Hằng', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='zhongli_card.png', cast=[LUMINE, PAIMON, ZHONGLI, CHILDE2, PING, QIQI, BAIZHU, GANYU, EKATERINA, SHITOU, YINGER],
       pdf='', footer='Chương I · Màn II — Lời Tạm Biệt Thể Xác Vĩnh Hằng', side=False),
  dict(id='c1-man3', arc='Chương I · Liyue', src='c1_man3.txt', act='Chương I · Màn III', title='Ngôi Sao Đang Đến', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='keqing_card.png', cast=[LUMINE, PAIMON, KEQING_C3, NINGGUANG_C3, GANYU_C3, ZHONGLI_C3, CHILDE_C3, SIGNORA_C3, XIAO_C3, ADEPTI_C3, PING_C3, OSIAL, MENGDAN],
       pdf='', footer='Chương I · Màn III — Ngôi Sao Đang Đến', side=False),
  dict(id='c1-man4-1', arc='Chương I · Liyue', src='c1_man4_1.txt', act='Chương I · Màn III.1', title='Ý Nghĩa Của Lupical', sub='Nhiệm vụ nhân vật bắt buộc để mở Chương I · Màn IV — Chương Tiểu Lang - Màn I (Razor)',
       hero='razor_card.png', cast=[LUMINE, PAIMON, RAZOR41, AMBER41, BOREAS41, VILLAGERS41, DRAFF],
       pdf='', footer='Chương I · Màn III.1 — Ý Nghĩa Của Lupical', side=True),
  dict(id='c1-man4-2', arc='Chương I · Liyue', src='c1_man4_2.txt', act='Chương I · Màn III.2', title='Gió, Đôi Cánh Và Dũng Khí', sub='Nhiệm vụ nhân vật bắt buộc để mở Chương I · Màn IV — Chương Tiểu Thố - Màn I (Amber)',
       hero='amber_splash.png', cast=[LUMINE, PAIMON, AMBER42, OTTO, RAPTOR, FARRAH],
       pdf='', footer='Chương I · Màn III.2 — Gió, Đôi Cánh Và Dũng Khí', side=True),
  dict(id='c1-man4-gt', arc='Chương I · Liyue', src='c1_man4_gt.txt', act='Chương I · Màn IV · Giới Thiệu', title='Dainsleif', sub='Nhiệm vụ mở đầu bắt buộc của Chương I · Màn IV — Người Giữ Cành',
       hero='dainsleif_banner.png', thumb='dainsleif_thumb.png', cast=[LUMINE, PAIMON, DAIN_GT, KATHERYNE, LAWRENCE, CHARLES],
       pdf='', footer='Chương I · Màn IV · Giới Thiệu — Dainsleif', side=True),
  dict(id='c1-man4', arc='Chương I · Liyue', src='c1_man4.txt', act='Chương I · Màn IV', title='Chúng Ta Ắt Sẽ Trùng Phùng', sub='Nhiệm vụ Ma Thần — Mondstadt và Liyue',
       hero='ganyu_card.png', cast=[LUMINE, PAIMON, DAIN4, GANYU4, LAN, HERALD, BARBARA4, ROSARIA, JEAN4, RAZOR, BOREAS, AETHER4],
       pdf='', footer='Chương I · Màn IV — Chúng Ta Ắt Sẽ Trùng Phùng', side=False),
  dict(id='c2-modau', arc='Chương II · Inazuma', src='c2_modau.txt', act='Chương II · Mở Đầu', title='Gió Thu Vén Áo Hỏi Lá Đỏ', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='kazuha_card.png', cast=[LUMINE, PAIMON, BEIDOU, KAZUHA, ATSUKO, ZHUHAN, CHUYUN, LINHSON, JINYOU, RONGSHI, FEI],
       pdf='', footer='Chương II · Mở Đầu — Gió Thu Vén Áo Hỏi Lá Đỏ', side=False),
  dict(id='c2-man1', arc='Chương II · Inazuma', src='c2_man1.txt', act='Chương II · Màn I', title='Lôi Thần Uy Nghiêm, Địa Đàng Vĩnh Hằng', sub='Nhiệm vụ Ma Thần — Inazuma',
       hero='ayaka_splash.png', cast=[LUMINE, PAIMON, THOMA, AYAKA, YOIMIYA, SARA, YAE, BEIDOU_C2, CHISATO, SHINSUKE, WERNER, KURISU, TEJIMA, KUROSAWA, DOMON, MASAKATSU],
       pdf='', footer='Chương II · Màn I — Lôi Thần Uy Nghiêm, Địa Đàng Vĩnh Hằng', side=False),
  dict(id='c2-man1-1', arc='Chương II · Inazuma', src='c2_man1_1.txt', act='Chương II · Màn I.1', title='Câu Chuyện Về Hạc Và Thỏ Trắng', sub='Nhiệm vụ nhân vật bắt buộc để mở Chương II · Màn II — Chương Tuyết Hạc - Màn I (Kamisato Ayaka)',
       hero='ayaka_splash.png', cast=[LUMINE, PAIMON, AYAKA11, OGURA, KURISU11, RONIN11, KIMINAMI, FESTIVAL],
       pdf='', footer='Chương II · Màn I.1 — Câu Chuyện Về Hạc Và Thỏ Trắng', side=True),
  dict(id='c2-man1-2', arc='Chương II · Inazuma', src='c2_man1_2.txt', act='Chương II · Màn I.2', title='Vĩnh hằng như một giấc mơ', sub='Nhiệm vụ nhân vật bắt buộc để mở Chương II · Màn II — Chương Lưu Kim - Màn I (Yoimiya)',
       hero='yoimiya_splash.png', cast=[LUMINE, PAIMON, YOIMIYA12, KIDS12, RYUUNOSUKE, SAKUJIROU, KOUICHI, MORIHIKO, AMENOMA, IMATANI, SATORU, KEISUKE, YOSHITAKA],
       pdf='', footer='Chương II · Màn I.2 — Vĩnh hằng như một giấc mơ', side=True),
  dict(id='c2-man2', arc='Chương II · Inazuma', src='c2_man2.txt', act='Chương II · Màn II', title='Tâm Vô Tạp Niệm, Bất Sinh Bất Diệt', sub='Nhiệm vụ Ma Thần — Inazuma',
       hero='raiden_splash.png', cast=[LUMINE, PAIMON, AYAKA2, THOMA2, RAIDEN, TEPPEI, GOROU, SARA2, KOKOMI, KAZUHA2, BEIDOU2, RESIST],
       pdf='', footer='Chương II · Màn II — Tâm Vô Tạp Niệm, Bất Sinh Bất Diệt', side=False),
  dict(id='c2-man3', arc='Chương II · Inazuma', src='c2_man3.txt', act='Chương II · Màn III', title='Thiên Thủ Bách Nhãn, Thiên Hạ Nhân Gian', sub='Nhiệm vụ Ma Thần — Inazuma',
       hero='raiden_nc.png', cast=[LUMINE, PAIMON, KOKOMI3, TEPPEI3, GOROU3, OOKUBO, KOUTOKU, SCARA, YAE3, SARA3, SAYU, THOMA3, AYAKA3, YOIMIYA3, TAKAYUKI, SIGNORA3, RAIDEN3, KAZUHA3],
       pdf='', footer='Chương II · Màn III — Thiên Thủ Bách Nhãn, Thiên Hạ Nhân Gian', side=False),
  dict(id='cd-man1', arc='Chương II · Inazuma', src='cd_man1.txt', act='Chương Đệm · Màn I', title='Phong Khởi Hạc Quy', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='shenhe_splash.png', cast=[LUMINE, PAIMON, SHENHE, YUNJIN, NINGGUANG_CD, BEIDOU_CD, CLOUD_CD, XINGQIU, BAIZHU_CD, KEQING_CD, BAIWEN, ZHANG, MINGJUN, BEISHT, LIU],
       pdf='', footer='Chương Đệm · Màn I — Phong Khởi Hạc Quy', side=False),
  dict(id='c2-man4', arc='Chương II · Inazuma', src='c2_man4.txt', act='Chương II · Màn IV', title='Khúc An Hồn Nơi Đáy Vực', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='c2m4_act.png', cast=[LUMINE, PAIMON, DAIN_C2M4, HALFDAN, AETHER_C2M4, KATHERYNE_C2M4, YUEHUI, HERALD_C2M4, LECTOR, BSK],
       pdf='', footer='Chương II · Màn IV — Khúc An Hồn Nơi Đáy Vực', side=False),
  dict(id='cd-man1-1', arc='Chương II · Inazuma', src='cd_man1_1.txt', act='Chương Đệm · Màn I.1', title='Hành Trình Bên Trong Vực Đá Sâu', sub='Nhiệm vụ thế giới bắt buộc để mở Chương Đệm · Màn II — Vực Đá Sâu, Liyue',
       hero='chasm.png', cast=[LUMINE, PAIMON, ZHIQIONG, MUNING, JINWU, KHEDIVE, CLITOPHO],
       pdf='', footer='Chương Đệm · Màn I.1 — Hành Trình Bên Trong Vực Đá Sâu', side=True),
  dict(id='cd-man2', arc='Chương II · Inazuma', src='cd_man2.txt', act='Chương Đệm · Màn II', title='Lộ Trình Nguy Hiểm', sub='Nhiệm vụ Ma Thần — Liyue',
       hero='yelan_splash.png', cast=[LUMINE, PAIMON, YELAN, YANFEI, ITTO, SHINOBU, USHI, XIAO_CD2, FUSHE, BOYANG, ZHONGLI_CD2],
       pdf='', footer='Chương Đệm · Màn II — Lộ Trình Nguy Hiểm', side=False),
  dict(id='c3-man1', arc='Chương III · Sumeru', src='c3_man1.txt', act='Chương III · Màn I', title='Xuyên Qua Màn Sương Và Rừng Rậm', sub='Nhiệm vụ Ma Thần — Sumeru',
       hero='c3m1_act.png', cast=[LUMINE, PAIMON, TIGHNARI, COLLEI, KIEMLAM, HAYPASIA, HERALD_C3, GIAOVIEN, PANAH, KATHERYNE_C3, DUNYARZAD, DEHYA, NILOU, ALHAITHAM, DORI, AYN, GIAOVIEN2],
       pdf='', footer='Chương III · Màn I — Xuyên Qua Màn Sương Và Rừng Rậm', side=False),
  dict(id='c3-man2', arc='Chương III · Sumeru', src='c3_man2.txt', act='Chương III · Màn II', title='Bình Minh Của Ngàn Đóa Hồng', sub='Nhiệm vụ Ma Thần — Sumeru',
       hero='c3m2_q2.png', cast=[LUMINE, PAIMON, DUNYARZAD2, DEHYA2, NILOU2, NAHIDA, KIMIYA, VIHAR, AZAR, SETARIA, BADIS, AMAL, OTHERS_C32],
       pdf='', footer='Chương III · Màn II — Bình Minh Của Ngàn Đóa Hồng', side=False),
]
