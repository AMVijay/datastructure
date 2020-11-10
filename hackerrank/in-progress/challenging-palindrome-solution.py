#
# Complete the buildPalindrome function below.
#
def buildPalindrome(a, b):

    palindrome = "-1"

    a_length = len(a)
    b_length = len(b)
        
    for a_index in range(a_length):
        max_end_index = b_length
        while max_end_index >= 0 and b.rfind(a[a_index],0,max_end_index) > -1:
            b_index = b.rindex(a[a_index],0,max_end_index)
            if (a_length - a_index) + b_index > len(palindrome) or (palindrome == "-1") or ((a_length - a_index) + b_index == len(palindrome) and a[a_index] < palindrome[0]):
                temp_palindrome = a[a_index] + b[b_index]
                
                offset = 1 
                while (a_index + offset) < a_length and (b_index - offset) >= 0 and a[a_index + offset] == b[b_index - offset]:
                    temp_palindrome = temp_palindrome[0:offset] + a[a_index+offset] + b[b_index-offset] + temp_palindrome[offset:]
                    offset = offset + 1

                # Find Max SubString in a
                a_start_index = a_index + offset
                temp_a_palindrome = ""
                if(a_start_index < a_length):
                    temp_a_palindrome = a[a_start_index]
                    a_max_end_index = a_length
                    while temp_a_palindrome == a[a_start_index] and a_max_end_index > a_start_index and a.rfind(a[a_start_index], a_start_index+1, a_max_end_index) > -1:
                        end_index = a.rindex(a[a_start_index], a_start_index+1,a_max_end_index)
                        compare_string = a[a_start_index:a_max_end_index+1]
                        if compare_string == compare_string[::-1]:
                            temp_a_palindrome = compare_string
                        
                        a_max_end_index = end_index
                        if a_max_end_index <= a_start_index:
                            break

                # Find max substring in b
                b_end_index = b_index - offset
                temp_b_palindrome = ""
                if b_end_index >= 0:
                    temp_b_palindrome = b[b_end_index]
                    b_max_start_index = 0 
                    while temp_b_palindrome == b[b_end_index] and b_end_index > b_max_start_index and b.find(b[b_end_index], b_max_start_index, b_end_index+1) > -1:
                        start_index = b.index(b[b_end_index], b_max_start_index, b_end_index+1)
                        compare_string = b[start_index:b_end_index+1]
                        if compare_string == compare_string[::-1]:
                            temp_b_palindrome = compare_string
                        
                        b_max_start_index = start_index + 1
                        if b_max_start_index == b_end_index:
                            break
                
                # if a_index == 14:
                # print("Derived Values1 ", a_index, a[a_index], palindrome, temp_palindrome, temp_a_palindrome, temp_b_palindrome)

                if len(temp_palindrome) + len(temp_a_palindrome) >= len(palindrome) or len(temp_palindrome) + len(temp_b_palindrome) >= len(palindrome):
                    if len(temp_a_palindrome) > 0 and len(temp_b_palindrome) > 0:
                        if len(temp_a_palindrome) == len(temp_b_palindrome):
                            if temp_a_palindrome < temp_b_palindrome:
                                temp_palindrome = temp_palindrome[0:offset] + temp_a_palindrome + temp_palindrome[offset:]
                            else:
                                temp_palindrome = temp_palindrome[0:offset] + temp_b_palindrome + temp_palindrome[offset:]

                        elif len(temp_a_palindrome) > len(temp_b_palindrome):
                            temp_palindrome = temp_palindrome[0:offset] + temp_a_palindrome + temp_palindrome[offset:]
                        else:
                            temp_palindrome = temp_palindrome[0:offset] + temp_b_palindrome + temp_palindrome[offset:]

                    elif len(temp_a_palindrome) > 0: 
                        temp_palindrome = temp_palindrome[0:offset] + temp_a_palindrome + temp_palindrome[offset:]
                    else:
                        temp_palindrome = temp_palindrome[0:offset] + temp_b_palindrome + temp_palindrome[offset:]

                # if a_index == 14:
                # print("Derived Values2 ", palindrome, a[a_index], temp_palindrome, temp_a_palindrome, temp_b_palindrome)

                if len(temp_palindrome) > len(palindrome):
                    palindrome = temp_palindrome
                else:
                    if len(palindrome) == len(temp_palindrome) and palindrome > temp_palindrome:
                        palindrome = temp_palindrome

            max_end_index = b_index
                
    return palindrome
  
# a = "abprstsyyyyqyyyys"
# b = "pbat"

# a = "bac"
# b = "bac"

# a = "abprstsyyys"
# b = "pbasyyyyqyyyyst"

# a="dczatfarqdkelalxzxillkfdvpfpxabqlngdscrentzamztvvcvrtcm"
# b="bqlizijdwtuyfrxolsysxlfebpolcmqsppmrfkyunydtmwbexsngxhwvroandfqjamzkpttslildlrkjoyrpxugiceahgiakev"

# a="zlc"
# b="zdw"

# a="def"
# b="abaf"

# a = "ab"
# b = "ba"

a = 'zzkbdgivaqismrzwzrirolxivizyppqzkwkbylhaugjmzfjtwroeyxgilqjvavmbnvnacclngqubsmcvunjucgfioptgoyykapnmepjdgjvmqjsqirrbvyqnokggyhpovlwmzwhwrejjwscgfipkmjthrdqoxquosqabzfzuuzajsmtxculipprztefmsehhjecneedirscuiltmygqnmaitiafoozliiluuymtrvilsswawpfpprfwbutkzmazbjwiidpszbmisizdprofirunfzwtbvvmusunigwyjvdnvkxgymrxriikyyjcrwozzmuyhgjhmmlnahjkvivbuatrykwsojhbagwlsjzqtnbomrugnhvbdvyewvnvhalvxueykbxrtdqrlyrryrxmbcvzahwuqwnfqrmksakubleisxlzgvqewgbeuprelfafutwacildojcaermoqnpvwwmzrajlfccaxwgkbcbualdufxhssfcrjtymfzuwnscuvswdafeblkfiszvgfhjwxhwqzchslfakrxiuzvqvkygmeqvgogzbufsptxmutxpzoaqqcpkokpaohxmknazavgzjzedbbkjygkyuaqbgvhpxbqpkexbumyhuyaimdizwzpzyelpbtjzapmllpewksjlcacvfnvjxcpgpckincgmdsseftjnugstnwbhnehmktshazfpzniwoimeuykivspupjbanmisbscdomuhlhpvworeicuuveovnzalfiaueumcgjyvduxupocubrbrhxzxxgykbzxhluqxzqhfhsiyopvstrtwvagtfkvjmfrwnyvkrkfqfinlgonngmhxvwrsggklsdsocqvgjkbagkcozzlltvzhsjgpuriyyslknfobecisdsdzwvuxoezgalvbhdtfbwaljcsfyfhiujluqoiuvncktvrvhwbarnvtrzvqfnfjekakkilhvxshugseegumlgjzecegklweststdytqklpdkmklckcnjwrrirqztqxemigiujdlbluedrqqdvwjnjbimzrhzevojqinaddpjvfwjnvgoncaojywmivydvqvskmqjrhdyhudkinplvkobpzoibiwhktqbwtrcaytawpmvujieztjymxgjvkguowmksticgftenjdxasllnptqwpnvdceohqyjxirwqngcuepcbtlkemwiqtrlcplnamxurqolatjubcyirazwifkfddrqnjdqfasgmuklgxzinapkiuwpswoyfgawulxsnufnfblzupgqeukmkqbhmjfkjhbjdudjhabjsmykaqpeigeyhwpgmjptrfhgzjyyvoskxdpwoxauppygnxdgdabypltpxaxunalzmugkjfkpjtmfhioasefuhtiohleaqmgondmyknzfceffdwfupigehmrxpihpvqodehrfuxeegzolcrdlieoxzxdqdkiatiaiqrorpqnrxkfqnldmsioxakzjszxxafddbagurzirhtynujhkrlcbblihbtcnsbbbtyfrewckksloocajybwwabqskxjduwmvbbniloereysasfewlwklzycgfhgmvhlzftcifkzuuhqtmdudcqersskxftnnpbtchgglhagkszenocwdsyektpubnwjscwsuybrszfzjcbuenvldqaonsjtltgbecnsafmfofmgajlveqrpfiwckkajlrrdsxneebhfrzfokmlgwpmaomhcjnymnhschjdbrjrwclxyzhkhksnbnrxrwkbznifkahqokxyogdtvhwqbjgtxchajtojbvhqoybghfhluyollnataaaqxfoftzfhlxaxsvwfbyvcblqcxchgyswfazbkfgauoatzhademcxxfkotnyvlnqzrlfdfnhwolchkbykodlkbpzdogwvovywwjpuvoffqznqgqlacyzkajxvqymeskdxbgqoimczqrnuymzsdicncplrmmvwzwowbggmgjpjheadyhdizgkidyogqpvndpkwgoastlnacihxyxnifldmlctofefcxryebxkuqnvigwuurkonwkgpnwmngoufnqkwnybnlkkvnuhuxgromslliiucwkmrdexfffqwwyvujharstsbpqrdecurcffubhqybfpzybrgopzxrmmsmdvpjalhgsqmctsxqhyspxsohlmgqlnibswxtfovcubquiswtcusigxyaywapffcueyyglitjewtzreooepvlbpuhfbioobpfqhfdfxqaxzfuwrwwdpemrlblttcgxodygfkwbuoalmavaggcyyxlmeucdlefmuebdknpzqiwnxpoquvcskegxwheqolrsotcxgxhpwrwnceguouxqlsecgyljuyrwndjndcasfvncupjjfnmjxmpsftyxctxiyuklxpdcxivqntnujkdvjsatecenwkslsztqtammhxjedvnbxepgrqhoqzmsvjwgahebthhvgxmvdtliuetlfdezfjmfntjtshztjrenruasedvzkeojadyowfdnvtrafkpngjbmpdpwkknahfqnrbpdelisixsgmxzikhfsgdxkkyovwppbexlgcphxmhvkivbbvbfobwufozkqzmkmslazvrjkdazomfyptwbfzctmxyrqbybudwnwhhtmbpeiydmpwayynkjitwwqhzeujzqvfbtpmskwbzkeqybaydxgbhpikvbopsbgwayiflfnadnxnsljilohkhefhkwbrjxljhlgsqdhkkuxckgtstsdgpofogxurjycnsiyxozjutwpxxcckrdjpbxmubgwfiirhhutwebdlnlpsnofqyvvkorzkercpeojxtiscksyrmbsjbuaqboiyvbaqfibdaswkngafyoydijwkgqmucegfstwlxbcnjolzslcndfbyxwamsozlyromjttblaaejxameifmvpnxxpwndygvjykqmwvixtsqmzshdjuacywfmnftlfbjdjvjiiszhoqxfcvzstmkhbekfwagpgyqzchabparixzaavdwkjhhxbbfepupndjqaapxtqlsjzvfpiyldiibemlpkeqilwogsqwhillgkedxzlmvlwfzwyyzesvmbjlyuqvqoamjiklnfetdnilsotkwmyewzoygdtdcnfywmuernjrswhwgrlrkzsaszgxbtejktoawkdshhwmitrxgzfqkpieowqomliowzwsjotamapcewlbyujlmhahtccjjlekmayzhdvcumdxxvwrzbelmqqetnhcfbeqmnsvlkkrewxlxnmvowesoprhwmwhvlziepgfthtendmfndexunllrbixqsaoajpzmbudgnpcgkjwlbvyrvqcdkqcrnrmbrtvsnscbcksycviwbpxuatpsssbrhlnbkunhafrebotrsheuvzhhocikzmyfmaqydwdzsscmnygszmyrvmlgntqxcostlnarfwskvdhaacwjmhewzpjrpvgabkwhxghvmlkjycczheyysusdmitckskjdirzwpmhyamqovfeqmqflrvjzasejueljiyxcbwyzvvsjuauhbdqkbjamqorkwjrneismebucbwbzebnrezceczuzouphocsfdqcvcreifihzhfunwvtcrbvchmghezvczvbhowyujgitrvmmtxvmivalwnsiaygdqqteqeukkjhpbfyqeecirmlefniotroypykcurqizzsydgbxojzmkijijdovmjbujmbwjhsskskrvvtmpzqqtijuneezzijrfzklpjvosvryciducsapzugarfeyopwalsdnwmraicrhqgkpasgztwgogdyddekukjcqwmjjwxdcftbgbcbzxkibxnegssyhnpjukqirnllacjzgivmfhjrqiezzdpsyyobwmbqryaecdelwwntnhhswubpuzdyhwitrwvqqjzgimgtjvehazdydsdsyjgsseorjrltszbxqiganalyygouhyfgmnazwxccnrbkohxzpnavwklwsomlhvmzklbxarexjszmhkfnypyjopvftswrqujezhndbqlktpnkfpdtfjijqorysinzcyvvpseyptyuechdkyqkafnbuagpikzwfskousupmuewyxrjrthfnjvexfotuveqmunbbrnzlrcsqxzzlndhjvotvmsnkpcawiziyglidwnstybkyndelpmzlyesiavoszfqmvdrrayqkczuaurhdunxsordeepwmijpwilmzmpicszqsezmtfijmjgimhyhuqwvnpardzapcqvoncupiwbqqxymgalwdekkkdqakdsbpuxfhxnmjtzbmifhqgphoooasoeapjjmafqjtthtfslruzjlltkozkxsxuejgcxwijgechahznxdnxxpvbjlonggjexpvkbmduwvampwapsqizmnagsntnqgeagkxohcoyomtrhkwxbckugkdwtfmixqyfrsxfsosztvwilrcxgmdsvdqithpmyezzwenwdemyxpoanbcffbtwklnrutxgrofelqwjdyfchrzetzenmukkafqgrbnrjszmarzsbvyhiramwzwbzisjqvbxgixkzfzbzualsgkvsbmshfnyejbiwimlxvtpotriuildfvyevqbxxxawjsettemhmghnwsesgwpgtxjurczbznbzjmlffjfdplndgdabktpuxcvuiebcctdkrydxurhvupxbhtvgqhhcmxrdbbyebverbxxibiiubsyayszqrxchxadszzetociuygpksnbsilfxrnouhclgzorzcjorjcyeehhehofzytiykqiwbqcrxsoieirxjfwtcnmvrxifxmfyculypbftjuzbdbzsmkrbkjjjhejmonpkijzksehtsgadqjwwbltbndpzozsjvrpqnemvahdjebhjxszsmoufjgcszfvxtpghaocabzvsdxlchdbsuvjfoyeudkfpecwyvxlwfpsfuuqcegwpzefgoasktgmrdltqkfyngpwfhierzvcaspyixexddfpjfgazwjpiaosqklsluimvcisvxmnuuvvxemmymhpcnvbcqjthlfnxcmqqidgdseamjprsptadtxdugfdlydjxffcdifuiszuhrznbdhspuloljbwpbapswzfivxdtgmptsyrwnruacoxykcqmotwpeubbhzdhhlwmopczzhmatpzqcrygxdgeoweatvhifxzcyazttnbmwckherbpafexnejizeektnmdhvupuizszohosahdxomrgqfgcqumhhjwhyrmuoqtxuaenwrpcaavqesoqodnuuuzixlvtnxdeqkthphpcasevkkouobqzadcgllqwzhabfmyvlpvltypgqqianiajtjusqdkkcwvifisaaymieumpzgkfiehjmujyrdtqdiyiuldwswqjgpinlyfcfyrktmbvlfonkkfczdsglwkrdqvaurmnbcnrzivffluqduosdcmewkwogmubysbmhbaazkbhyzhiwxiiwmpwvasnefevjhwleunabsjvikshwybwtjsrkjrzmtzvcwpcndvrheijqlqcpsjmrxsywhkkdergjoaphniisoandcsvcijcfbeaptmeztqpcdkguhjwsmhloxmpgjpeceysnucphrmpfnrvjnlkflxdycjymufxfixxkcfpgrczogtguluwftavuvanxghgnzomyrighjhafqxgfkotwuffgizapokdcpzmvzlivfctmuznchicihjvvqrfbelvdqxivjuvulzpqzruaqouksadaitjrblkvewovqehzlporgifghesapiztwnoppexaozpvatvptrqliqdnpufupjtgggyjegmqejhnhwczauylvliwxsealqkadlmcfvwobdplefcuwsebfwkyxiywdnwlwbbsnubmiotrncazkjjpvnossmejxuaaccfyqslhxqceqwqvzlunjkmmrupjqkbqfgqbcccmdiqyhjwwxftnbyvnwpkotzbhdtzqicerxogfazjjfnlhadvedlkgsfzwjsqskevrrnwfwszvexapojsklgkjbiudarbdsilhlaznqabiyejohhuqxjapppyisuhypbowexqnrgrppldstzsmrpldiyrpvgctaxgpppaoylzccexfwnwfwshzuxdckalspmfjcdglpsbpwogridvoftxxgjkykvmwqtpjxqnswizepirqoxtosrtptkulexgxesurfkerwsnjzjztgmkivngrpsxekffovjxihyjjfrdzdasiuxcgrlhcsijmqqugtoazifxalyekcjlnxkqnzkfuihkwjsmnzscguzwsdxwritiyvdcunbnjiotfkwqtknwszbpltuinwyohoudkeaglxbelvtpjyvatmamzhoghxndxdloonobcbjerykojnlfzkuyuzfsknhyglvpdyotzeijcxdqfefirykzhpvragspiqfwmdbxitdwnegsphyzcsbsodlnutppngbnvtzuxbitxlszffgsystbtylndftclsjarpczauvmovlffudrxkzxwetaaofhfphnxpruhqzfdhxvpylohdovfniosdzfbjrufwpjlpmgxjohgaynlozytsmfbpabvsmnueblmywevrliwpveieklwbvboctirbeepvoiiqtpcffqvnpssenhgamqoyufrshqlbcnbdgtqxjkouwedgwvlnlegqilxnumvqstpxfkkvbadtpwfqowbomvxtqhyddowqhwgnovzoojiurllebjdvwmafscgritlrnryzgwwthfvkhcwrhqrcbuhjviprgiqjlqaznpggvvwzzlaedglinffomspntneceaahpyyxycvdrzzoihjoimpwxsmbpfmjkiwbdbprazcxxkkhhsvtlgerjdraryekkntbnxzdtrvimshdnjioxvpgxvqpfmbijuzpzmjwlzlabnleatpwtkusdpnovxrwxjcfermiailxdxpqqgwpphsheyidefvkvegxcxslcweessznkviakiwlvppriojqkenfdiyaaxcnveomawslzsnhrcojjsvrurtrftrqckmgzzltqmemwnqmczcvmfoqchiwxbsjipssqhpjqqrszucmtdjlnjqvrhjmugsbnksqkuhdhbaroxxmbbhpocexsvubtmifwskmbminwchmjewdwwkmrwsppsxemjnaubwqtjhicwcbhfstbrwtqrilrcykgvvjkqcsbfqitknygmlnhckqgmvfrjbjmlhyiwdrfnukoweopwqvabwhcjxypkflgwodmidimnunqvouujnjdrylcphnelguqwzdllgngmcwttpidaaxvhuzaxpoyaqpkgdjgypdznhkclryjdipgmhdqzmoggtlglurkujqyglhsnoliyytzonrwoxgcizyxjrjqomydiidpefluaqklgxrnlkkaafqefdxuztwasdkguexfxkjlnmqyouaogpytjdnfkoelexxaapxccsxjksfqlkhvrmhikshlmftesgqxgatdkrwcltyichwmvznfugopevxamskgvvawdmyteyzbnqvyabwkwqdspoiwqvwqehleshjymroeqekbpacoqdmmtefgqkstqxsruawhacgbrgsjibypiohhjlpayosyaxtxfzmvntqhmsozgejfkawztzeavlduxwnldpecqmkjtvjztypfmrvaecugejmamcunvlooilfljkhhmeymkcaiysappwppswdjinmbixpnltctjsnbssyxkmsmfzvtoaukqpqriqwvlhbxlriavssflopodxycqvzsnkowsmnwoilrdmdktpgsskzbluzbrgdjrumqjfiwsihrariazdqykualuwdftnatlojvpdifxfrvxexyvfjhqhhgueybzilnovcoltvykfjvliomdvizvzqlpsroluzdcfjpdftjnnrtzezmungtwccvljmucvgxmjoyonhqtzylocbeitpzqqahwgddczemkbockfsriqajhvffohrnivazapnibsnculskuxenanpfpvolrmryfcudbzxgasgxkpvcxxdlbrbnvxhvjoallkmlfrwobxocktpjgycljbnkbrhxmmyyrnzpqcmdwwdragqmmwxysxvsugwfcjdulgkyejzbqtnmugtocvznhegxaveuzcwiahxdntwxunqoaaxkvlovvqykevptuyfnthykzbfgireqacgcuyyucbzqufxelbdjugwpyvjyzpihuxuvfmjtlixzvxjkhbdsnjpydlrfuiyquwphewmrut'
b = 'uriarvrcnimdeplhtadpjgtxfosuwsqokbiphrlpylyvdmxtztyyriojrqwjkruuykqqhgqzsfksrhygijlxudccyiwtevoemhzpqjuoesplqloeuspngsiawvqgxjtplhvfcwkpjdvmfyisjqitoymrianbfjnyeowkpguugtbvqxgbfhijihtydhfwdudoeipvindapvptmmjdezydeytslmodfcfwgdcpuakseezocainjidtsypwhgxmcvtjdljsjvppseuuazbuouzrpxyqdpkhhtinyadechyaqyrytbcyozaxlsaksyqtwsrosontrkpdqwwqafcchrqrvtddoapxhptpogvzlmmtgodrzcerkrymvjyvwnnwgyyujebhywnnnwtzyyqtbtfzwysufdrmkuihkaabzmzhmmyaxbpnrjbxcunwizljeufyfrabgtdmwpuygrkoruekzxcocxobrgzetajwhtjazncdxfvmiklchqyxenblolekgduywwpsucaawiachpdtshhynfjcbalxzrcclhnrruttlyqtbhobsxxzmrbxmimnsyrwqynhjpofmdyijmuhrjzpsnwutmebaxnujqtgmaxkqvqzquvirckrsaynvtsunizvitomnrwcfxvlbryjmwyfzmzsukqsbsqklujdhkdamsibagqmvgmogffidhpofuycsewdvhhirydzwxdhnpnpwhcbklrxkipqstjlssxspngqfkzsqynxnesbonwxzqdffgtnxbtguqenqflqvuicwfnfpmkfbqxmoqtjzxzvehwgrejopmneyeypztvgbairrmcctcylvzaujoznwihzajjbqglcmpswrbuhweyclcyewhubrwspmclgqbjjazhiwnzojuazvlyctccmrriabgvtzpyeyenmpojergwhevzxzjtqomxqbfkmpfnfwciuvqlfqnequgtbxntgffdqzxwnobsenxnyqszkfqgnpsxssljtsqpikxrlkbchwpnpnhdxwzdyrihhvdwescyufophdiffgomgvmqgabismadkhdjulkqsbsqkuszmzfywmjyrblvxfcwrnmotivzinustvnyasrkcrivuqzqvqkxamgtqjunxabemtuwnspzjrhumjiydmfopjhnyqwrysnmimxbrmzxxsbohbtqyltturrnhlccrzxlabcjfnyhhstdphcaiwaacuspwwyudgkelolbnexyqhclkimvfxdcnzajthwjatezgrboxcocxzkeurokrgyupwmdtgbarfyfuejlziwnucxbjrnpbxaymmhzmzbaakhiukmrdfusywzftbtqyyztwnnnwyhbejuyygwnnwvyjvmyrkreczrdogtmmlzvgoptphxpaoddtvrqrhccfaqwwqdpkrtnosorswtqyskaslxazoycbtyryqayhcedaynithhkpdqyxprzuoubzauuesppvjsjldjtvcmxghwpystdijniacozeeskaupcdgwfcfdomlstyedyzedjmmtpvpadnivpieodudwfhdythijihfbgxqvbtguugpkwoeynjfbnairmyotiqjsiyfmvdjpkwcfvhlptjxgqvwaisgnpsueolqlpseoujqpzhmeovetwiyccduxljigyhrskfszqghqqkyuurkjwqrkxaaoqnuxwtndxhaiwczuevaxgehnzvcotgumntqbzjeykgludjcfwgusvxsyxwmmqgardwwdmcqpznryymmxhrbknbjlcygjptkcoxbowrflmkllaojvhxvnbrbldxxcvpkxgsagxzbducfyrmrlovpfpnanexukslucnsbinpazavinrhoffvhjaqirsfkcobkmezcddgwhaqqzptiebcolyztqhnoyojmxgvcumjlvccwtgnumzeztrnnjtfdpjfcdzulorsplqzvzivdmoilvjfkyvtlocvonlizbyeughhqhjfvyxexvrfxfidpvjoltantfdwulaukyqdzairarhiswifjqmurjdgrbzulbzkssgptkdmdrliownmswoknszvqcyxdopolfssvairlxbhlvwqirqpqkuaotvzfmsmkxyssbnsjtctlnpxibmnijdwsppwppasyiackmyemhhkjlflioolvnucmamjeguceavrmfpytzjvtjkmqcepdlnwxudlvaeztzwakfjegzosmhqtnvmzfxtxaysoyapljhhoipybijsgrbgcahwaursxqtskqgfetmmdqocapbkeqeormyjhselheqwvqwiopsdqwkwbayvqnbzyetymdwavvgksmaxvepogufnzvmwhciytlcwrkdtagxqgsetfmlhskihmrvhklqfskjxsccxpaaxxeleokfndjtypgoauoyqmnljkxfxeugkdsawtzuxdfeqfaakklnrxglkqaulfepdiidymoqjrjxyzicgxowrnoztyyilonshlgyqjukrulgltggomzqdhmgpidjyrlckhnzdpygjdgkpqayopxazuhvxaadipttwcmgnglldzwquglenhpclyrdjnjuuovqnunmidimdowglfkpyxjchwbavqwpoewokunfrdwiyhlmjbjrfvmgqkchnlmgynktiqfbscqkjvvgkycrlirqtwrbtsfhbcwcihjtqwbuanjmexsppswrmkwwdwejmhcwnimbmkswfimtbuvsxecophbbmxxorabhdhukqsknbsgumjhrvqjnljdtmcuzsrqqjphqsspijsbxwihcqofmvczcmqnwmemqtlzzgmkcqrtfrtrurvsjjocrhnszlswamoevncxaayidfnekqjoirppvlwikaivknzsseewclsxcxgevkvfediyehshppwgqqpxdxliaimrefcjxwrxvonpdsuktwptaelnbalzlwjmzpzujibmfpqvxgpvxoijndhsmivrtdzxnbtnkkeyrardjregltvshhkkxxczarpbdbwikjmfpbmsxwpmiojhiozzrdvcyxyyphaaecentnpsmoffnilgdealzzwvvggpnzaqljqigrpivjhubcrqhrwchkvfhtwwgzyrnrltirgcsfamwvdjbellruijoozvongwhqwoddyhqtxvmobwoqfwptdabvkkfxptsqvmunxliqgelnlvwgdewuokjxqtgdbncblqhsrfuyoqmaghnesspnvqffcptqiiovpeebritcobvbwlkeievpwilrvewymlbeunmsvbapbfmstyzolnyaghojxgmpljpwfurjbfzdsoinfvodholypvxhdfzqhurpxnhpfhfoaatewxzkxrdufflvomvuazcprajslctfdnlytbtsysgffzslxtibxuztvnbgnpptunldosbsczyhpsgenwdtixbdmwfqipsgarvphzkyrifefqdxcjieztoydpvlgyhnksfzuyukzflnjokyrejbcbonooldxdnxhgohzmamtavyjptvlebxlgaekduohoywniutlpbzswnktqwkftoijnbnucdvyitirwxdswzugcsznmsjwkhiufkznqkxnljckeylaxfizaotguqqmjischlrgcxuisadzdrfjjyhixjvoffkexsprgnvikmgtzjzjnswrekfrusexgxeluktptrsotxoqripeziwsnqxjptqwmvkykjgxxtfovdirgowpbsplgdcjfmpslakcdxuzhswfwnwfxecczlyoapppgxatcgvpryidlprmsztsdlpprgrnqxewobpyhusiypppajxquhhojeyibaqnzalhlisdbraduibjkglksjopaxevzswfwnrrveksqsjwzfsgkldevdahlnfjjzafgoxreciqztdhbztokpwnvybntfxwwjhyqidmcccbqgfqbkqjpurmmkjnulzvqwqecqxhlsqyfccaauxjemssonvpjjkzacnrtoimbunsbbwlwndwyixykwfbeswucfelpdbowvfcmldakqlaesxwilvlyuazcwhnhjeqmgejygggtjpufupndqilqrtpvtavpzoaxepponwtzipasehgfigroplzheqvowevklbrjtiadaskuoqaurzqpzluvujvixqdvlebfrqvvjhicihcnzumtcfvilzvmzpcdkopazigffuwtokfgxqfahjhgirymoznghgxnavuvatfwulugtgozcrgpfckxxifxfumyjcydxlfklnjvrnfpmrhpcunsyecepjgpmxolhmswjhugkdcpqtzemtpaebfcjicvscdnaosiinhpaojgredkkhwysxrmjspcqlqjiehrvdncpwcvztmzrjkrsjtwbywhskivjsbanuelwhjvefensavwpmwiixwihzyhbkzaabhmbsybumgowkwemcdsoudqulffvizrncbnmruavqdrkwlgsdzcfkknoflvbmtkryfcfylnipgjqwswdluiyidqtdryjumjheifkgzpmueimyaasifivwckkdqsujtjainaiqqgpytlvplvymfbahzwqllgcdazqbouokkvesacphphtkqedxntvlxizuuundoqoseqvaacprwneauxtqoumryhwjhhmuqcgfqgrmoxdhasohozsziupuvhdmntkeezijenxefapbrehkcwmbnttzayczxfihvtaewoegdxgyrcqzptamhzzcpomwlhhdzhbbuepwtomqckyxocaurnwrystpmgtdxvifzwspabpwbjlolupshdbnzrhuzsiufidcffxjdyldfgudxtdatpsrpjmaesdgdiqqmcxnflhtjqcbvncphmymmexvvuunmxvsicvmiulslkqsoaipjwzagfjpfddxexiypsacvzreihfwpgnyfkqtldrmgtksaogfezpwgecquufspfwlxvywcepfkdueyofjvusbdhclxdsvzbacoahgptxvfzscgjfuomszsxjhbejdhavmenqprvjszozpdnbtlbwwjqdagstheskzjikpnomjehjjjkbrkmszbdbzujtfbpylucyfmxfixrvmnctwfjxrieiosxrcqbwiqkyityzfohehheeycjrojczrozglchuonrxflisbnskpgyuicotezzsdaxhcxrqzsyaysbuiibixxbrevbeybbdrxmchhqgvthbxpuvhruxdyrkdtccbeiuvcxuptkbadgdnlpdfjfflmjzbnzbzcrujxtgpwgseswnhgmhmettesjwaxxxbqveyvfdliuirtoptvxlmiwibjeynfhsmbsvkgslauzbzfzkxigxbvqjsizbwzwmarihyvbszramzsjrnbrgqfakkumneztezrhcfydjwqleforgxturnlkwtbffcbnaopxymedwnewzzeymphtiqdvsdmgxcrliwvtzsosfxsrfyqximftwdkgukcbxwkhrtmoyochoxkgaegqntnsganmziqspawpmavwudmbkvpxejggnoljbvpxxndxnzhahcegjiwxcgjeuxsxkzoktlljzurlsfthttjqfamjjpaeosaooohpgqhfimbztjmnxhfxupbsdkaqdkkkedwlagmyxqqbwipucnovqcpazdrapnvwquhyhmigjmjiftmzesqzscipmzmliwpjimwpeedrosxnudhruauzckqyarrdvmqfzsovaiseylzmplednykbytsnwdilgyiziwacpknsmvtovjhdnlzzxqscrlznrbbnumqevutofxevjnfhtrjrxyweumpusuoksfwzkipgaubnfakqykdhceuytpyespvvycznisyroqjijftdpfknptklqbdnhzejuqrwstfvpojypynfkhmzsjxeraxblkzmvhlmoswlkwvanpzxhokbrnccxwzanmgfyhuogyylanagiqxbzstlrjroessgjysdsdydzahevjtgmigzjqqvwrtiwhydzupbuwshhntnwwledceayrqbmwboyyspdzzeiqrjhfmvigzjcallnriqkujpnhyssgenxbikxzbcbgbtfcdxwjjmwqcjkukeddydgogwtzgsapkgqhrciarmwndslawpoyefraguzpascudicyrvsovjplkzfrjizzeenujitqqzpmtvvrksksshjwbmjubjmvodjijikmzjoxbgdyszziqruckypyortoinfelmriceeqyfbphjkkueqetqqdgyaisnwlavimvxtmmvrtigjuywohbvzcvzehgmhcvbrctvwnufhzhifiercvcqdfscohpuozuzceczernbezbwbcubemsienrjwkroqmajbkqdbhuaujsvvzywbcxyijleujesazjvrlfqmqefvoqmayhmpwzridjkskctimdsusyyehzccyjklmvhgxhwkbagvprjpzwehmjwcaahdvkswfranltsocxqtnglmvrymzsgynmcsszdwdyqamfymzkicohhzvuehsrtoberfahnukbnlhrbsssptauxpbwivcyskcbcsnsvtrbmrnrcqkdcqvryvblwjkgcpngdubmzpjaoasqxibrllnuxednfmdnethtfgpeizlvhwmwhrposewovmnxlxwerkklvsnmqebfchnteqqmlebzrwvxxdmucvdhzyamkeljjccthahmljuyblwecpamatojswzwoilmoqwoeipkqfzgxrtimwhhsdkwaotkjetbxgzsaszkrlrgwhwsrjnreumwyfncdtdgyozweymwktoslindtefnlkijmaoqvquyljbmvsezyywzfwlvmlzxdekgllihwqsgowliqekplmebiidlyipfvzjslqtxpaaqjdnpupefbbxhhjkwdvaazxirapbahczqygpgawfkebhkmtszvcfxqohzsiijvjdjbfltfnmfwycaujdhszmqstxivwmqkyjvgydnwpxxnpvmfiemaxjeaalbttjmorylzosmawxybfdnclszlojncbxlwtsfgecumqgkwjidyoyfagnkwsadbifqabvyiobqaubjsbmryskcsitxjoepcrekzrokvvyqfonsplnldbewtuhhriifwgbumxbpjdrkccxxpwtujzoxyisncyjruxgofopgdststgkcxukkhdqsglhjlxjrbwkhfehkholijlsnxndanflfiyawgbspobvkiphbgxdyabyqekzbwksmptbfvqzjuezhqwwtijknyyawpmdyiepbmthhwnwdubybqryxmtczfbwtpyfmozadkjrvzalsmkmzqkzofuwbofbvbbvikvhmxhpcglxebppwvoykkxdgsfhkizxmgsxisiledpbrnqfhankkwpdpmbjgnpkfartvndfwoydajoekzvdesaurnerjtzhstjtnfmjfzedflteuiltdvmxgvhhtbehagwjvsmzqohqrgpexbnvdejxhmmatqtzslskwnecetasjvdkjuntnqvixcdpxlkuyixtcxytfspmxjmnfjjpucnvfsacdnjdnwryujlygceslqxuougecnwrwphxgxctosrloqehwxgekscvuqopxnwiqzpnkdbeumfeldcuemlxyycggavamlaoubwkfgydoxgcttlblrmepdwwrwufzxaqxfdfhqfpbooibfhupblvpeooerztwejtilgyyeucffpawyayxgisuctwsiuqbucvoftxwsbinlqgmlhosxpsyhqxstcmqsghlajpvdmsmmrxzpogrbyzpfbyqhbuffcrucedrqpbstsrahjuvywwqfffxedrmkwcuiillsmorgxuhunvkklnbynwkqnfuognmwnpgkwnokruuwgivnqukxbeyrxcfefotclmdlfinxyxhicanltsaogwkpdnvpqgoydikgzidhydaehjpjgmggbwowzwvmmrlpcncidszmyunrqzcmioqgbxdksemyqvxjakzycalqgqnzqffovupjwwyvovwgodzpbkldokybkhclowhnfdflrzqnlvyntokfxxcmedahztaouagfkbzafwsyghcxcqlbcvybfwvsxaxlhfztfofxqaaatanlloyulhfhgbyoqhvbjotjahcxtgjbqwhvtdgoyxkoqhakfinzbkwrxrnbnskhkhzyxlcwrjrbdjhcshnmynjchmoampwglmkofzrfhbeenxsdrrljakkcwifprqevljagmfofmfasncebgtltjsnoaqdlvneubcjzfzsrbyuswcsjwnbuptkeysdwconezskgahlgghctbpnntfxkssreqcdudmtqhuuzkfictfzlhvmghfgcyzlkwlwefsasyereolinbbvmwudjxksqbawwbyjacoolskkcwerfytbbbsnctbhilbbclrkhjunythrizrugabddfaxxzsjzkaxoismdlnqfkxrnqprorqiaitaikdqdxzxoeildrclozgeexufrhedoqvphipxrmhegipufwdffecfznkymdnogmqaelhoithufesaoihfmtjpkfjkgumzlanuxaxptlpybadgdxngyppuaxowpdxksovyyjzghfrtpjmgpwhyegiepqakymsjbahjdudjbhjkfjmhbqkmkueqgpuzlbfnfunsxluwagfyowspwuikpanizxglkumgsafqdjnqrddfkfiwzariycbujtaloqruxmanlpclrtqiwmekltbcpeucgnqwrixjyqhoecdvnpwqtpnllsaxdjnetfgcitskmwougkvjgxmyjtzeijuvmpwatyacrtwbqtkhwibiozpbokvlpnikduhydhrjqmksvqvdyvimwyjoacnogvnjwfvjpddaniqjovezhrzmibjnjwvdqqrdeulbldjuigimexqtzqrirrwjnckclkmkdplkqtydtstsewlkgecezjglmugeesguhsxvhlikkakejfnfqvzrtvnrabwhvrvtkcnvuioquljuihfyfscjlawbftdhbvlagzeoxuvwzdsdsicebofnklsyyirupgjshzvtllzzockgabkjgvqcosdslkggsrwvxhmgnnoglnifqfkrkvynwrfmjvkftgavwtrtsvpoyishfhqzxqulhxzbkygxxzxhrbrbucopuxudvyjgcmueuaiflaznvoevuucierowvphlhumodcsbsimnabjpupsvikyuemiowinzpfzahstkmhenhbwntsgunjtfessdmgcnikcpgpcxjvnfvcacljskwepllmpazjtbpleyzpzwzidmiayuhymubxekpqbxphvgbqauykgyjkbbdezjzgvazankmxhoapkokpcqqaozpxtumxtpsfubzgogvqemgykvqvzuixrkaflshczqwhxwjhfgvzsifklbefadwsvucsnwuzfmytjrcfsshxfudlaubcbkgwxaccfljarzmwwvpnqomreacjodlicawtufaflerpuebgweqvgzlxsielbukaskmrqfnwquwhazvcbmxryrrylrqdtrxbkyeuxvlahvnvweyvdbvhngurmobntqzjslwgabhjoswkyrtaubvivkjhanlmmhjghyumzzowrcjyykiirxrmyexhkzfnhdaonyrnnjohsjxfxcgfrsfocixpzrzliephjpzxbmvhlqatlgddkqcxzhqqvuly'

print(buildPalindrome(a,b))