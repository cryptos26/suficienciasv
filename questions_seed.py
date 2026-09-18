"""
Banco de datos de casos prácticos y preguntas especializadas para el Examen
de Suficiencia de Notariado de la Corte Suprema de Justicia de El Salvador.
Fundamentación rigurosa con base en:
- Ley de Notariado (LN)
- Ley del Ejercicio Notarial de la Jurisdicción Voluntaria y de Otras Diligencias (LENJVOD)
- Código Civil de El Salvador (C.C.)
- Código de Familia (C.F.)
- Código Procesal Civil y Mercantil (CPCM)
- Código de Comercio (C.Com.)
- Ley de Reestructuración Municipal y normativa registral (CNR)
"""

CATEGORIES = [
    {
        "id": "notariado_puro",
        "name": "Ley de Notariado y Función Notarial",
        "description": "Protocolo, escrituras matrices, actas, testimonios, inhabilitaciones y formalidades solemnes.",
        "icon": "scroll"
    },
    {
        "id": "jurisdiccion_voluntaria",
        "name": "Jurisdicción Voluntaria Notarial (LENJVOD)",
        "description": "Aceptación de herencia, remedición de inmuebles, rectificación de partidas y diligencias no contenciosas.",
        "icon": "scale"
    },
    {
        "id": "civil_sucesiones",
        "name": "Derecho Civil y Régimen Sucesorio",
        "description": "Testamentos abiertos y cerrados, asignaciones forzosas, porción conyugal, contratos e hipotecas.",
        "icon": "book-open"
    },
    {
        "id": "familia_menores",
        "name": "Derecho de Familia y Menores",
        "description": "Matrimonio en sede notarial, regímenes patrimoniales, divorcio por mutuo acuerdo y poderes familiares.",
        "icon": "users"
    },
    {
        "id": "mercantil_societario",
        "name": "Derecho Mercantil y Títulos Valores",
        "description": "Constitución de sociedades de capital y personas, poderes mercantiles, protesto de cheques y pagarés.",
        "icon": "building-2"
    },
    {
        "id": "registral_cnr",
        "name": "Derecho Registral y Catastro (CNR)",
        "description": "Principios registrales, tracto sucesivo, calificación registral, subsanación y cancelaciones de gravámenes.",
        "icon": "archive"
    }
]

QUESTIONS = [
    # --- 1. LEY DE NOTARIADO PURO ---
    {
        "category_id": "notariado_puro",
        "question": "Comparece ante un notario salvadoreño una persona de 35 años que desea otorgar una donación irrevocable de un inmueble. Al solicitarle su documento de identidad, el otorgante manifiesta que extravió su Documento Único de Identidad (DUI) hace dos días y exhibe únicamente su Pasaporte Salvadoreño vigente y su Licencia de Conducir. ¿Puede el notario autorizar la escritura matriz con tales documentos de identificación?",
        "option_a": "Sí, porque el pasaporte es un documento oficial con fotografía emitido por el Estado que acredita la identidad de cualquier ciudadano salvadoreño.",
        "option_b": "No; tratándose de salvadoreños en el territorio de la República, el único documento legal para identificarse ante notario es el DUI, salvo que el notario lo conozca personalmente o se recurra a dos testigos de conocimiento.",
        "option_c": "Sí, siempre y cuando el notario relacione la Licencia de Conducir y agregue copia certificada de la misma al legajo de anexos del protocolo.",
        "option_d": "No, el notario debe suspender el acto de inmediato y no puede bajo ninguna circunstancia celebrar el instrumento hasta que el otorgante tramite su nuevo DUI.",
        "correct_option": "B",
        "legal_basis": "Ley de Notariado, Art. 32 ord. 5° y Ley Especial Reguladora de la Emisión del Documento Único de Identidad (DUI).",
        "justification": "De conformidad con el Art. 32 ord. 5° de la Ley de Notariado, el notario debe dar fe del conocimiento de los comparecientes. Si no los conoce personalmente, debe identificarlos por medio de su Documento de Identidad personal. Tratándose de salvadoreños mayores de edad domiciliados en la República, el DUI es el único documento legalmente idóneo para acreditar identidad civil; el pasaporte solo es admisible para salvadoreños residentes en el extranjero o extranjeros. No obstante, si el otorgante carece de DUI en el momento, la ley notarial salvadoreña faculta expresamente al notario a suplir la falta mediante dos testigos de conocimiento que conozcan al compareciente y sean conocidos del notario, o si el notario mismo lo conoce personalmente, lo cual hace falsa la opción D y plenamente correcta la B.",
        "distractors_analysis": "La Opción A es incorrecta porque la jurisprudencia de la CSJ y la normativa del DUI establecen que el pasaporte salvadoreño no sustituye al DUI para actos jurídicos solemnes dentro del país cuando se es residente nacional. La Opción C es incorrecta porque la licencia de conducir no constituye documento de identidad personal notarial idóneo según la Ley de Notariado. La Opción D es incorrecta porque olvida la figura del conocimiento personal directo del notario o el auxilio de dos testigos de conocimiento idóneos conforme al Art. 32 ord. 5° LN.",
        "difficulty": "Media"
    },
    {
        "category_id": "notariado_puro",
        "question": "En una escritura de compraventa de un inmueble, la parte compradora es una persona que no sabe firmar debido a que es analfabeta. ¿Cuál es la formalidad y procedimiento notarial que exige la Ley de Notariado para la validez de dicho instrumento matriz?",
        "option_a": "Basta con que el comprador estampe la huella digital de su pulgar derecho en la escritura matriz, sin necesidad de testigos ni firmas adicionales.",
        "option_b": "Debe comparecer obligatoriamente un testigo instrumental, quien firmará a su ruego, y además el notario debe hacer comparecer a un abogado que asista al otorgante.",
        "option_c": "El comprador estampará su huella dactilar de uno de sus dedos (de preferencia el pulgar derecho), y a su ruego firmará una persona de su elección, pudiendo ser uno de los dos testigos instrumentales que obligatoriamente deben concurrir al acto.",
        "option_d": "El notario no puede autorizar una compraventa donde una de las partes no sabe firmar, debiendo remitirse al juzgado civil para que nombre un curador especial.",
        "correct_option": "C",
        "legal_basis": "Ley de Notariado, Arts. 32 ord. 12° y 34 inciso 1°.",
        "justification": "El Art. 32 ord. 12° de la Ley de Notariado establece que si alguno de los otorgantes no supiere o no pudiere firmar, estampará la huella digital de alguno de sus dedos, de preferencia el pulgar de la mano derecha, y firmará a su ruego otra persona. Asimismo, el Art. 34 inciso 1° de la misma ley ordena de manera perentoria la presencia obligatoria de DOS testigos instrumentales cuando alguno de los otorgantes no sepa o no pueda firmar, pudiendo uno de estos testigos firmar a su ruego.",
        "distractors_analysis": "La Opción A es incorrecta porque omite la firma a ruego y la concurrencia imperativa de testigos instrumentales (Art. 34 LN). La Opción B es incorrecta porque inventa la figura de un 'abogado asistente' no contemplada en la Ley de Notariado y reduce erróneamente los testigos a uno solo. La Opción D es un error conceptual grave: el analfabeto es plenamente capaz civilmente para otorgar contratos y no requiere curador judicial.",
        "difficulty": "Media"
    },
    {
        "category_id": "notariado_puro",
        "question": "Un notario concluye las veinticinco hojas de su libro de protocolo el día 10 de octubre de 2024. Según el mandato taxativo de la Ley de Notariado salvadoreña, ¿cuál es el plazo y el trámite legal que debe seguir respecto al libro de protocolo agotado?",
        "option_a": "Debe conservarlo en su poder hasta que se cumpla exactamente un año desde la fecha de entrega del libro por parte de la Sección de Notariado.",
        "option_b": "Debe poner la razón de cierre inmediatamente y remitirlo a la Sección del Notariado de la CSJ dentro de los quince días siguientes a la fecha en que se agotó.",
        "option_c": "Tiene un plazo de treinta días hábiles para solicitar hojas adicionales a la Dirección General de Tesorería para continuar el mismo libro.",
        "option_d": "Puede retener el libro agotado en su archivo particular de por vida, remitiendo únicamente un índice certificado de las escrituras otorgadas.",
        "correct_option": "B",
        "legal_basis": "Ley de Notariado, Art. 21 inciso 2° y Art. 24.",
        "justification": "Conforme al Art. 21 y Art. 24 de la Ley de Notariado, cuando un libro de protocolo se agota antes del año de vigencia, el notario pondrá la razón de cierre expresando el número de hojas y de escrituras autorizadas, y lo entregará a la Sección del Notariado dentro de los quince días siguientes a aquel en que se agotó o terminó. La omisión de este plazo acarrea multas y eventuales sanciones disciplinarias por parte de la Corte Plena de la CSJ.",
        "distractors_analysis": "La Opción A es incorrecta porque la retención del libro agotado durante el resto del año está expresamente prohibida; una vez agotado, opera el plazo perentorio de 15 días. La Opción C es incorrecta porque en El Salvador no se agregan hojas a un libro ya formado y agotado. La Opción D confunde la custodia del protocolo; en El Salvador los protocolos son propiedad del Estado y el notario solo es su depositario temporal.",
        "difficulty": "Difícil"
    },
    {
        "category_id": "notariado_puro",
        "question": "¿En cuál de los siguientes casos incurre el notario en una infracción sancionada con la nulidad absoluta del instrumento público por inobservancia de prohibición legal de otorgamiento?",
        "option_a": "Cuando autoriza una escritura pública en la cual comparece como parte compradora su propio cónyuge o sus parientes dentro del cuarto grado de consanguinidad o segundo de afinidad.",
        "option_b": "Cuando autoriza una escritura pública en día domingo o en horas no hábiles de la noche.",
        "option_c": "Cuando autoriza un poder judicial fuera de su despacho u oficina notarial permanente.",
        "option_d": "Cuando expide un segundo testimonio sin que el primero haya sido devuelto por el interesado.",
        "correct_option": "A",
        "legal_basis": "Ley de Notariado, Art. 9 y Art. 10.",
        "justification": "El Art. 9 de la Ley de Notariado prohíbe de manera terminante al notario autorizar instrumentos en que resulte o pueda resultar algún provecho directo para él, para su cónyuge, o para sus ascendientes, descendientes o hermanos, o sus parientes dentro del cuarto grado de consanguinidad o segundo de afinidad. El Art. 10 sanciona los instrumentos autorizados en contravención al Art. 9 con la nulidad absoluta de los mismos, sin perjuicio de la responsabilidad disciplinaria e indemnizatoria.",
        "distractors_analysis": "La Opción B es incorrecta porque la función notarial salvadoreña no está restringida a días u horas hábiles administrativas; el notario ejerce fe pública 24/7. La Opción C es incorrecta porque el notario goza de fe pública en todo el territorio nacional y puede autorizar instrumentos en cualquier lugar. La Opción D es incorrecta porque el notario está legalmente facultado para expedir ulteriores testimonios a favor de las partes interesadas según el Art. 44 LN.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "notariado_puro",
        "question": "Un notario autoriza una escritura matriz de donación. Posteriormente advierte que omitió consignar el estado familiar y la profesión de uno de los donatarios. Las hojas de su protocolo aún están en su poder y no ha cerrado el libro. ¿Puede el notario subsanar esta deficiencia agregando una nota al margen del instrumento matriz por sí solo?",
        "option_a": "Sí, el notario tiene facultades discrecionales para testar o enmendar de oficio cualquier dato secundario antes de cerrar el libro.",
        "option_b": "No; una vez firmado el instrumento por las partes y autorizado por el notario, no puede hacerse en él ninguna alteración, raspadura, interlineado ni entrerrenglonadura; cualquier adición o rectificación debe hacerse mediante una nueva escritura pública de aclaración o rectificación con comparecencia de las partes.",
        "option_c": "Sí, siempre y cuando ponga una razón que diga 'Vale lo testado' y selle con su sello notarial autorizado por la CSJ.",
        "option_d": "Sí, si se trata de datos de identificación civil, basta con que el notario levante un acta notarial fuera del protocolo y la agregue al legajo de anexos.",
        "correct_option": "B",
        "legal_basis": "Ley de Notariado, Art. 35 y Art. 36.",
        "justification": "De acuerdo con el Art. 35 y 36 de la Ley de Notariado, una vez firmado el instrumento por los otorgantes y autorizado por el notario, este no puede alterar, enmendar ni agregar texto al instrumento matriz. Las enmendaduras y testaduras solo son válidas si se salvan al final del instrumento y ANTES de las firmas de los comparecientes. Toda modificación o subsanación posterior exige el otorgamiento de una nueva escritura matriz de rectificación o aclaración.",
        "distractors_analysis": "La Opción A y la Opción C son erróneas: las notas de 'valga' posteriores a las firmas son nulas y constituyen falta grave de alteración del protocolo. La Opción D es incorrecta porque un acta notarial por separado no puede enmendar ni alterar una escritura matriz de protocolo.",
        "difficulty": "Difícil"
    },
    {
        "category_id": "notariado_puro",
        "question": "Conforme a la Ley de Notariado, ¿cuál de los siguientes actos NO PUEDE constar válidamente en un Acta Notarial y exige de manera forzosa el otorgamiento de Escritura Pública?",
        "option_a": "El protesto de un cheque por falta de fondos o de una letra de cambio.",
        "option_b": "La notificación de la revocación de un mandato otorgado por instrumento público.",
        "option_c": "La promesa unilateral o bilateral de venta de un inmueble situado en El Salvador.",
        "option_d": "La comprobación de hechos materiales que el notario presencie o constate personalmente.",
        "correct_option": "C",
        "legal_basis": "Ley de Notariado, Art. 50 y Art. 51 en relación con el Art. 1605 y Art. 1425 del Código Civil.",
        "justification": "El Art. 50 de la Ley de Notariado establece expresamente que en las actas notariales se consignarán los hechos y actos que el notario presencie o que ante él se ejecuten o pasen, pero prohíbe tajantemente autorizar en actas notariales contratos y actos jurídicos solemnes que deban celebrarse en escritura matriz. La promesa de venta de un inmueble y los contratos traslaticios de dominio son actos sustantivos de carácter patrimonial que requieren escritura pública matriz para su plena validez jurídica.",
        "distractors_analysis": "Las opciones A, B y D son actos típicamente formalizados mediante Acta Notarial según los Arts. 50 y 51 de la Ley de Notariado y las leyes especiales mercantiles (protesto de cheques en acta, notificación de revocación en acta, y constancia de hechos materiales presenciados).",
        "difficulty": "Media"
    },

    # --- 2. JURISDICCIÓN VOLUNTARIA NOTARIAL (LENJVOD) ---
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "En unas diligencias notariales de aceptación de herencia intestada tramitadas conforme a la LENJVOD, el notario ha recibido la solicitud y mandó a publicar los edictos de ley. ¿Cuántas veces y en qué medios deben publicarse dichos edictos?",
        "option_a": "Una sola vez en el Diario Oficial y una vez en un diario de circulación nacional.",
        "option_b": "Tres veces en el Diario Oficial y tres veces en uno de los diarios de mayor circulación de la República.",
        "option_c": "Dos veces en el Diario Oficial y una vez en el tablero de avisos de la alcaldía municipal del domicilio del causante.",
        "option_d": "Tres veces consecutivas exclusivamente en el Diario Oficial, sin necesidad de periódico particular.",
        "correct_option": "B",
        "legal_basis": "Ley del Ejercicio Notarial de la Jurisdicción Voluntaria y de Otras Diligencias (LENJVOD), Art. 19 inciso 2°.",
        "justification": "El Art. 19 inciso 2° de la LENJVOD dispone textualmente que admitida la solicitud y comprobada la calidad de heredero, el notario mandará fijar un edicto en su oficina y publicará el mismo tres veces en el Diario Oficial y tres veces en uno de los diarios de mayor circulación nacional, citando a quienes se crean con derecho a la herencia para que se presenten a deducirlo dentro del término de quince días contados desde el día siguiente a la tercera publicación en el Diario Oficial.",
        "distractors_analysis": "La Opción A reduce ilegalmente las publicaciones a una. La Opción C confunde trámites judiciales con el régimen notarial. La Opción D omite el diario de circulación nacional, cuya omisión es causal de nulidad procesal y observación registral en el CNR al momento de inscribir la declaratoria definitiva de heredero.",
        "difficulty": "Media"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "Se presentan ante el notario dos hermanos para aceptar la herencia intestada de su padre. Tras la segunda publicación del edicto en el Diario Oficial, comparece al despacho notarial un tercer hijo del causante oponiéndose terminantemente a las diligencias notariales y manifestando que él es el único heredero legítimo. Ante este supuesto de controversia, ¿cuál es la obligación legal del notario según la LENJVOD?",
        "option_a": "El notario debe abrir a pruebas por el término de ocho días, recibir la prueba documental y dictar una resolución definitiva asignando los porcentajes correspondientes.",
        "option_b": "El notario debe suspender el trámite únicamente por 30 días para instar a las partes a conciliar en su oficina; si no concilian, declara herederos a los tres por partes iguales.",
        "option_c": "Cesa de inmediato la función notarial en el asunto; el notario debe abstenerse de seguir actuando y remitir todo el expediente original al juez de primera instancia competente.",
        "option_d": "El notario rechaza la oposición de plano por no haberse hecho en sede judicial, y continúa hasta expedir el testimonio de declaratoria de heredero a los dos solicitantes originales.",
        "correct_option": "C",
        "legal_basis": "LENJVOD, Art. 2.",
        "justification": "El Art. 2 de la LENJVOD consagra el principio medular del consentimiento unánime: las diligencias notariales solo proceden mientras exista conformidad absoluta de todas las partes interesadas. Si en cualquier estado del trámite surge controversia, oposición o discordia, cesa de pleno derecho la competencia notarial y el notario está obligado a abstenerse de continuar y remitir inmediatamente las actuaciones al Juez de Primera Instancia que corresponda.",
        "distractors_analysis": "La Opción A y B son falsas porque el notario salvadoreño en jurisdicción voluntaria carece absolutamente de jurisdicción contenciosa (potestad de resolver litigios o declarar derechos disputados bajo contienda). La Opción D constituiría una vulneración gravísima al debido proceso y al Art. 2 LENJVOD, que acarrea responsabilidad civil y penal.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "En unas diligencias notariales de Remedición de Inmueble tramitadas al amparo del Art. 15 de la LENJVOD, el notario cita a los colindantes para la inspección y mensura técnica pericial. Uno de los colindantes registrados se niega a recibir la esquela de citación. ¿Cómo debe proceder legalmente el notario salvadoreño?",
        "option_a": "El notario da por notificado al colindante rebelde fijando la esquela en la puerta de entrada de la propiedad del colindante, asistido por dos testigos.",
        "option_b": "La oposición a recibir la citación o la falta de notificación legal de todos los colindantes vicia el trámite; si el colindante no es legalmente citado o formaliza oposición al deslinde/remedición, el notario debe abstenerse y remitir las diligencias al Juez competente.",
        "option_c": "El notario prescinde de la citación de ese colindante siempre que el perito agrimensor declare bajo juramento que los linderos físicos no se modifican.",
        "option_d": "El notario solicita auxilio inmediato de la Policía Nacional Civil para obligar al colindante a comparecer a la diligencia.",
        "correct_option": "B",
        "legal_basis": "LENJVOD, Art. 15 en relación con el Art. 2.",
        "justification": "La citación legal de la totalidad de los colindantes es un requisito esencial de validez en las diligencias de remedición (Art. 15 LENJVOD). La falta de citación o la oposición de cualquiera de ellos a la mensura o a los linderos priva al notario de competencia, debiendo cesar en sus actuaciones y remitir el expediente al Juez de Primera Instancia. Catastro y el Registro de la Propiedad Raíz e Hipotecas rechazan de plano la inscripción de remediciones donde conste oposición de colindantes o vicios en su citación.",
        "distractors_analysis": "La Opción A aplica erróneamente normas de emplazamiento judicial del CPCM que no rigen de forma idéntica en el régimen consensual de la LENJVOD. La Opción C es ilegal porque la citación de colindantes no es subsanable por el dicho del perito. La Opción D es absurda: el notario no ejerce coactio ni imperio para ordenar detenciones o compulsión policial.",
        "difficulty": "Difícil"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "¿Puede un notario salvadoreño tramitar y otorgar un Título Supletorio respecto de un inmueble que carece de antecedente inscrito, cuando el poseedor acredite más de treinta años de posesión quieta, pacífica e ininterrumpida?",
        "option_a": "Sí, de conformidad con la LENJVOD, toda diligencia de titulación sobre bienes rústicos o urbanos puede seguirse ante notario.",
        "option_b": "No; las diligencias de titulación supletoria están reservadas con exclusividad a la sede judicial (ante el Juez de Primera Instancia Civil) conforme al Código Civil y la LENJVOD no facultó al notario para este trámite.",
        "option_c": "Sí, pero únicamente si el inmueble tiene un valor catastral menor a cien mil colones o su equivalente en dólares.",
        "option_d": "Sí, siempre y cuando intervenga como perito un ingeniero civil o arquitecto colegiado activo.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Art. 699 y siguientes; y exclusiones de la LENJVOD.",
        "justification": "Esta es una de las preguntas trampa clásicas del examen de notariado de la CSJ. La Ley del Ejercicio Notarial de la Jurisdicción Voluntaria y de Otras Diligencias (LENJVOD) enumera taxativamente las diligencias que pueden seguirse ante notario (herencias, remedición, deslinde voluntario, rectificación de partidas, etc.). En ningún artículo facultó a los notarios para tramitar Títulos Supletorios. Conforme al Art. 699 C.C., la titulación supletoria es competencia estricta y privativa del Órgano Judicial.",
        "distractors_analysis": "Las opciones A, C y D son falsas porque confunden la titulación supletoria (exclusiva de jueces de primera instancia) con la remedición de inmuebles que ya cuentan con título inscrito (esta última sí atribuida a notarios por el Art. 15 LENJVOD).",
        "difficulty": "Difícil"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "Concluidas unas diligencias de rectificación de partida de nacimiento en sede notarial por haberse consignado erróneamente el nombre de la madre, ¿cuál es el acto conclusivo que debe realizar el notario según la LENJVOD?",
        "option_a": "Debe autorizar una escritura pública de rectificación y remitir el libro de protocolo a la alcaldía.",
        "option_b": "Dicta una resolución final fundamentada en el acta respectiva y expide certificación notarial de dicha resolución a la oficina del Registro del Estado Familiar correspondiente para su asiento y marginación.",
        "option_c": "Envía el expediente original al Ministerio de Gobernación para que apruebe la rectificación.",
        "option_d": "El notario se traslada personalmente a la Alcaldía a tachar la partida original en el libro del registro.",
        "correct_option": "B",
        "legal_basis": "LENJVOD, Art. 11 y Art. 12; Ley Transitoria del Registro del Estado Familiar.",
        "justification": "Conforme al Art. 11 y 12 de la LENJVOD, en las diligencias de rectificación de partidas de estado familiar, el notario practica las pruebas documentales y testimoniales en actas notariales fuera del protocolo; comprobado el error u omisión, dicta una resolución final y de ella expide testimonio o certificación notarial que remite al funcionario del Registro del Estado Familiar correspondiente para que practique la marginación o asentamiento respectivo.",
        "distractors_analysis": "La Opción A es incorrecta porque las diligencias no se otorgan en escritura matriz de protocolo sino en expediente notarial de actas. La Opción C menciona una autoridad inconexa. La Opción D es manifiestamente ilícita: el notario jamás puede alterar materialmente los libros públicos de una municipalidad.",
        "difficulty": "Media"
    },

    # --- 3. DERECHO CIVIL Y SUCESIONES ---
    {
        "category_id": "civil_sucesiones",
        "question": "El testamento solemne abierto otorgado ante notario en El Salvador requiere para su validez la concurrencia obligatoria y presencial de:",
        "option_a": "Dos testigos presenciales de cualquier nacionalidad y mayores de 16 años.",
        "option_b": "Tres testigos instrumentales idóneos, que sepan leer y escribir, domiciliados en el lugar del otorgamiento, en un solo acto ininterrumpido.",
        "option_c": "Cinco testigos presenciales si el otorgamiento se realiza fuera de la capital de la República.",
        "option_d": "No requiere testigos instrumentales, bastando la fe pública del notario autorizante salvo que el testador sea analfabeto.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Art. 996 y Art. 999; Ley de Notariado, Art. 34 inciso 2°.",
        "justification": "Conforme al Art. 996 del Código Civil y Art. 34 inciso 2° de la Ley de Notariado, el testamento solemne abierto ante notario debe otorgarse ante TRES testigos instrumentales idóneos. Dicho acto debe realizarse en un solo contexto ininterrumpido (unidad de acto), con lectura en voz alta por el notario, presencia simultánea del testador y de los tres testigos de principio a fin.",
        "distractors_analysis": "La Opción A es incorrecta porque los testigos de testamento en El Salvador deben ser tres (salvo el testamento abierto sin notario ante juez que exige cinco, Art. 996 C.C.) y ser mayores de 18 años hábiles. La Opción C confunde las formalidades del testamento sin notario. La Opción D es falsa porque el testamento nunca prescinde de testigos instrumentales en la legislación salvadoreña.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "civil_sucesiones",
        "question": "¿Cuál de las siguientes personas se encuentra LEGALMENTE INHABILITADA para comparecer como testigo instrumental en un testamento solemne otorgado ante un notario salvadoreño?",
        "option_a": "Un amigo de la infancia del testador que reside en el mismo municipio del otorgamiento.",
        "option_b": "El cónyuge, los dependientes económicos o los parientes del notario autorizante dentro del cuarto grado de consanguinidad o segundo de afinidad.",
        "option_c": "Una persona salvadoreña de 65 años que sabe leer y escribir y no tiene vínculo familiar con las partes.",
        "option_d": "El patrono o empleador del testador que no recibe beneficio patrimonial alguno en la sucesión.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Art. 999 ord. 8° y Ley de Notariado Art. 34.",
        "justification": "El Art. 999 ordinal 8° del Código Civil enumera como inhábiles para ser testigos testamentarios al cónyuge y parientes del notario autorizante dentro del cuarto grado de consanguinidad o segundo de afinidad, así como a sus dependientes económicos o asalariados. Si alguno de ellos actúa como testigo instrumental, el testamento adolece de nulidad solemne absoluta.",
        "distractors_analysis": "Las opciones A, C y D corresponden a personas legalmente hábiles para testificar en actos solemnes, al no concurrir en ellas ninguna de las prohibiciones de parentesco, dependencia o incapacidad sensorial/mental del Art. 999 C.C.",
        "difficulty": "Media"
    },
    {
        "category_id": "civil_sucesiones",
        "question": "En el Derecho Civil salvadoreño vigente, respecto a la libertad de testar y las asignaciones forzosas, ¿cuál de las siguientes afirmaciones es jurídicamente correcta?",
        "option_a": "El testador salvadoreño está obligado a dejar las cuatro quintas partes de sus bienes como legítima rigurosa a sus hijos legítimos o naturales.",
        "option_b": "Existe plena libertad de testar, pero el testador está obligado por ley a respetar únicamente los alimentos forzosos debidos por ley y la porción conyugal si concurren las circunstancias legales.",
        "option_c": "En El Salvador rige el sistema de mejora testamentaria obligatorio de la legislación española decimonónica.",
        "option_d": "La ley salvadoreña prohíbe desheredar a los descendientes bajo cualquier causa o motivo.",
        "correct_option": "B",
        "legal_basis": "Código Civil de El Salvador, Arts. 1172, 1173 y 1174.",
        "justification": "Una particularidad fundamental del Derecho Civil salvadoreño (a diferencia de otros ordenamientos derivados del Código de Bello como Chile o Colombia) es que El Salvador derogó las legítimas rigurosas y cuartas de mejoras hace más de un siglo. Rige un sistema de amplia libertad testamentaria, condicionado únicamente al cumplimiento de las asignaciones forzosas: los alimentos legales debidos por el causante y la Porción Conyugal (Art. 1172 y ss. C.C.).",
        "distractors_analysis": "Las opciones A y C describen regímenes forzosos ajenos al Código Civil salvadoreño vigente. La Opción D es incorrecta porque el Código Civil contempla causales taxativas de desheredamiento de los legitimarios que tengan derecho a alimentos (Art. 1121 C.C.).",
        "difficulty": "Difícil"
    },
    {
        "category_id": "civil_sucesiones",
        "question": "En un contrato de compraventa con pacto de retroventa sobre un bien inmueble situado en San Salvador, las partes pactan que el vendedor podrá recobrar la cosa pagando el precio fijado en un plazo de siete años. Conforme al Código Civil salvadoreño, ¿qué efecto produce dicha estipulación del plazo?",
        "option_a": "El pacto de retroventa es nulo absolutamente por exceder de cuatro años, y vicia de nulidad todo el contrato de compraventa.",
        "option_b": "El contrato de compraventa es válido, pero el plazo del pacto de retroventa se reduce de pleno derecho a cuatro años, que es el plazo legal máximo perentorio permitido por la ley salvadoreña.",
        "option_c": "El plazo de siete años es plenamente eficaz en virtud del principio de autonomía de la voluntad privada.",
        "option_d": "El plazo se computará como prescripción adquisitiva ordinaria de diez años.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Art. 1683.",
        "justification": "El Art. 1683 del Código Civil salvadoreño prescribe taxativamente que el tiempo para intentar la acción de retroventa no podrá pasar de cuatro años contados desde la fecha del contrato. Si las partes hubieren estipulado un plazo mayor (como siete años), el pacto no anula la compraventa, sino que la cláusula temporal se reduce de pleno derecho al término legal máximo de cuatro años.",
        "distractors_analysis": "La Opción A es incorrecta porque el exceso en el plazo no acarrea la nulidad del contrato traslaticio ni del pacto en sí, sino su reducción legal imperativa. La Opción C es incorrecta porque las normas sobre plazos extintivos del Art. 1683 C.C. son de orden público patrimonial. La Opción D confunde figuras sustantivas.",
        "difficulty": "Difícil"
    },

    # --- 4. DERECHO DE FAMILIA Y MENORES ---
    {
        "category_id": "familia_menores",
        "question": "Un notario salvadoreño autoriza un matrimonio civil en la ciudad de Santa Tecla el día 15 de marzo. De acuerdo con el mandato conjunto del Código de Familia y la LENJVOD, ¿cuál es el plazo fatal para que el notario remita el testimonio respectivo al Registro del Estado Familiar de la alcaldía correspondiente, y cuál es la consecuencia de omitirlo?",
        "option_a": "Tiene quince días hábiles contados a partir del siguiente al de la celebración; su omisión o retraso le acarrea responsabilidad administrativa y sanción de multa impuesta por la autoridad municipal.",
        "option_b": "Tiene un plazo indefinido mientras no se cierre su libro de protocolo anual.",
        "option_c": "Debe remitirlo dentro de los tres días siguientes únicamente a la Sección del Notariado de la CSJ.",
        "option_d": "El notario no tiene obligación de remitir testimonios; es carga exclusiva de los contrayentes.",
        "correct_option": "A",
        "legal_basis": "Código de Familia, Art. 28; LENJVOD, Art. 14; Ley Transitoria del Registro del Estado Familiar.",
        "justification": "El Art. 28 del Código de Familia y el Art. 14 de la LENJVOD ordenan al funcionario autorizante (incluido el notario) remitir testimonio del acta de matrimonio a la alcaldía municipal del lugar de celebración, y de los lugares de nacimiento de los cónyuges, dentro de los quince días hábiles siguientes al de la celebración del matrimonio. El retraso o incumplimiento constituye infracción sancionada con multa por la municipalidad y responsabilidad disciplinaria ante la Sección del Notariado.",
        "distractors_analysis": "La Opción B es completamente falsa: el plazo de 15 días hábiles es perentorio. La Opción C confunde la alcaldía municipal con la Sección de Notariado de la CSJ (a la CSJ solo se remite el libro cerrado, no los avisos de matrimonios). La Opción D contradice la naturaleza de la fe pública notarial delegada por el Estado.",
        "difficulty": "Media"
    },
    {
        "category_id": "familia_menores",
        "question": "Dos cónyuges comparecen ante notario solicitando que tramite su Divorcio por Mutuo Consentimiento en sede notarial conforme a la Ley del Ejercicio Notarial de la Jurisdicción Voluntaria. La pareja tiene dos hijos en común: uno de 14 años y otro de 9 años. ¿Puede el notario autorizar dicho divorcio?",
        "option_a": "Sí, siempre y cuando los padres otorguen previamente un convenio de alimentos y régimen de visitas certificado por la Procuraduría General de la República (PGR).",
        "option_b": "No; el divorcio con existencia de hijos menores de edad o incapaces está reservado de manera absoluta e inderogable a la sede judicial ante los Juzgados de Familia correspondientes.",
        "option_c": "Sí, si los dos cónyuges nombran al notario como apoderado especial mancomunado.",
        "option_d": "Sí, pero debe publicar tres edictos en el Diario Oficial convocando a la PGR.",
        "correct_option": "B",
        "legal_basis": "Código de Familia, Arts. 106 ord. 1°, 108 y 109; y límites de competencia notarial en El Salvador.",
        "justification": "En la legislación salvadoreña, el divorcio por mutuo consentimiento donde existan hijos menores de edad no emancipados o personas con discapacidad dependientes debe ser decretado indispensablemente por un Juez de Familia (Art. 106 ord. 1° y Art. 108 Código de Familia), quien tiene el deber legal tutelar de velar por el interés superior del niño y aprobar el convenio regulador de alimentos, cuidado personal y régimen de comunicación. Ningún notario puede autorizar un divorcio existiendo hijos menores de edad.",
        "distractors_analysis": "La Opción A es una trampa muy común: la intervención o visto bueno de la PGR no habilita la sede notarial para disolver el vínculo matrimonial cuando hay menores; debe ser judicial. Las opciones C y D carecen de asidero legal en el ordenamiento salvadoreño.",
        "difficulty": "Media"
    },
    {
        "category_id": "familia_menores",
        "question": "En las capitulaciones matrimoniales otorgadas en escritura pública antes de la celebración del matrimonio, los futuros contrayentes no seleccionan expresamente ninguno de los regímenes patrimoniales previstos en el Código de Familia. Conforme a la ley familiar salvadoreña, ¿qué régimen patrimonial regirá su matrimonio por mandato supletorio?",
        "option_a": "El régimen de Separación de Bienes.",
        "option_b": "El régimen de Comunidad Diferida.",
        "option_c": "El régimen de Participación en las Ganancias.",
        "option_d": "El régimen de Sociedad Conyugal ilimitada del Código Civil de 1860.",
        "correct_option": "B",
        "legal_basis": "Código de Familia de El Salvador, Art. 41 y Art. 51.",
        "justification": "El Art. 41 del Código de Familia establece que a falta de capitulaciones matrimoniales o si estas resultaren ineficaces o insuficientes para determinar el régimen económico del matrimonio, se entenderá que los cónyuges quedan sujetos al régimen de COMUNIDAD DIFERIDA por ministerio de ley (régimen legal supletorio en El Salvador).",
        "distractors_analysis": "La Opción A (Separación de Bienes) y la Opción C (Participación en las Ganancias) solo aplican si las partes las pactan expresamente en escritura matriz de capitulaciones. La Opción D hace referencia a una figura jurídica derogada con la entrada en vigor del Código de Familia en 1994.",
        "difficulty": "Fácil"
    },

    # --- 5. DERECHO MERCANTIL Y TÍTULOS VALORES ---
    {
        "category_id": "mercantil_societario",
        "question": "Se constituye ante sus oficios notariales una Sociedad Anónima de Capital Variable (S.A. de C.V.) con un capital social pactado de VEINTE MIL DÓLARES. Conforme al Código de Comercio salvadoreño, ¿cuál es el porcentaje mínimo legal del capital social que debe pagarse efectivamente al momento del otorgamiento de la escritura de constitución?",
        "option_a": "Debe pagarse el cien por ciento (100%) mediante depósito bancario o cheque certificado.",
        "option_b": "Debe pagarse por lo menos el cinco por ciento (5%) de cada acción suscrita si es pagadera en dinero en efectivo.",
        "option_c": "Debe pagarse por lo menos el veinticinco por ciento (25%) del importe de cada acción pagadera en dinero efectivo.",
        "option_d": "Debe pagarse por lo menos el cincuenta por ciento (50%) en el acto y el resto en un plazo máximo de cinco años.",
        "correct_option": "B",
        "legal_basis": "Código de Comercio, Art. 192 numeral II.",
        "justification": "El Art. 192 numeral II del Código de Comercio de El Salvador (reformado por el D.L. N° 641 de 2008) establece expresamente que para la constitución de una sociedad anónima se requiere que el capital social no sea menor de dos mil dólares, y que si el capital se paga en dinero efectivo, se pague íntegramente por lo menos el CINCO POR CIENTO (5%) del valor de cada acción pagadera en numerario. (Anteriormente la norma histórica exigía el 25%, reforma que suele evaluar la CSJ para medir actualización normativa).",
        "distractors_analysis": "La Opción C (25%) era el régimen antiguo antes de las reformas de modernización mercantil para facilitar la creación de empresas en El Salvador. La Opción A aplica para el capital mínimo inicial cuando este sea de dos mil dólares pagados al 100% o bienes en especie. La Opción D carece de respaldo legal en la normativa societaria vigente.",
        "difficulty": "Difícil"
    },
    {
        "category_id": "mercantil_societario",
        "question": "Un notario es requerido para levantar el Acta Notarial de Protesto de un Cheque por falta de fondos. ¿Cuál es el plazo perentorio legal que establece el Código de Comercio para levantar el protesto por falta de pago de dicho título valor?",
        "option_a": "El protesto debe levantarse antes de la expiración del plazo de presentación para el pago (quince días), o dentro de los tres días hábiles siguientes al de la presentación.",
        "option_b": "Tiene hasta seis meses contados desde la fecha de emisión del cheque bancario.",
        "option_c": "Tiene exactamente veinticuatro horas a partir de la negativa de la entidad bancaria pagadora.",
        "option_d": "Los cheques en El Salvador ya no son susceptibles de protesto notarial bajo ninguna circunstancia.",
        "correct_option": "A",
        "legal_basis": "Código de Comercio de El Salvador, Art. 811 en relación con los Arts. 740 y 742.",
        "justification": "Conforme al Art. 811 del Código de Comercio, el protesto de un cheque por falta de pago debe tener lugar antes de que expire el plazo de presentación (que para cheques librados en el país es de quince días naturales, Art. 808 C.Com.) o dentro de los tres días hábiles siguientes a la expiración de dicho plazo o de la fecha de la oportuna presentación. El levantamiento del protesto en acta notarial es indispensable para conservar las acciones de regreso cambiarias si el banco no hubiere estampado la razón con valor de protesto.",
        "distractors_analysis": "La Opción B confunde el plazo de prescripción de la acción cambiaria de cheques con el plazo para levantar el acta de protesto. La Opción C es un plazo propio de otros ordenamientos o de aceptación de letras. La Opción D es falsa: el protesto notarial subsiste plenamente en el Código de Comercio.",
        "difficulty": "Difícil"
    },

    # --- 6. DERECHO REGISTRAL Y CATASTRO (CNR) ---
    {
        "category_id": "registral_cnr",
        "question": "El notario autoriza una escritura matriz de Compraventa de un inmueble. Días después de presentada al Registro de la Propiedad Raíz e Hipotecas (CNR), el registrador califica el documento y emite una resolución con observación por discordancia en la descripción técnica catastral. De acuerdo con la Ley de Reestructuración del Registro de la Propiedad Raíz e Hipotecas y el Reglamento del CNR, ¿qué plazo tiene el notario o interesado para subsanar dicha observación antes de que caduque el asiento de presentación?",
        "option_a": "Quince días hábiles contados a partir del retiro del testimonio.",
        "option_b": "Treinta días hábiles contados a partir del día siguiente a la notificación de la observación registral.",
        "option_c": "Sesenta días hábiles contados a partir de la notificación de la resolución registral denegatoria o suspensiva.",
        "option_d": "Un año calendario conforme a las reglas del tracto sucesivo.",
        "correct_option": "B",
        "legal_basis": "Reglamento de la Ley de Reestructuración del Registro de la Propiedad Raíz e Hipotecas, Art. 21 y Art. 22.",
        "justification": "El Art. 21 y 22 del Reglamento de la Ley de Reestructuración del Registro de la Propiedad Raíz e Hipotecas dispone que notificada una observación que impida la inscripción definitiva, el interesado dispone de un término de TREINTA DÍAS HÁBILES para retirar, subsanar y reingresar el instrumento debidamente corregido. Si transcurre dicho término sin subsanarse, el asiento de presentación caduca de pleno derecho perdiéndose la prioridad registral.",
        "distractors_analysis": "Las opciones A, C y D señalan plazos erróneos. El plazo de 30 días hábiles es el estándar registral salvadoreño vigente en el CNR para salvaguardar el principio de prioridad registral de los asientos de presentación.",
        "difficulty": "Media"
    },
    {
        "category_id": "registral_cnr",
        "question": "En la escritura matriz de Cancelación de Hipoteca Abierta otorgada por una institución bancaria a favor de un deudor que ha cancelado la totalidad de sus obligaciones crediticias, ¿cuál es el requisito formal indispensable que debe relacionar y hacer constar el notario autorizante para su debida inscripción en el CNR?",
        "option_a": "La comparecencia personal obligatoria del deudor hipotecario firmando de conformidad el instrumento de cancelación.",
        "option_b": "La personería jurídica legítima del apoderado o representante del banco acreedor, la determinación exacta de la inscripción de la hipoteca en el Registro, y la declaración expresa de quedar extinguida la obligación principal y cancelado el gravamen hipotecario.",
        "option_c": "Una constancia del Ministerio de Hacienda de solvencia tributaria del inmueble emitida con no más de doce horas de antelación.",
        "option_d": "La protocolización de los pagarés cancelados como parte integral del instrumento matriz.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Arts. 2180 y 2182; Ley de Notariado, Art. 32; y Ley de Reestructuración Registral.",
        "justification": "La cancelación de hipoteca es un acto unilateral otorgado por el acreedor o su apoderado con facultad suficiente. El notario debe legitimar la personería del representante bancario (conforme al Art. 32 ord. 11° LN), describir e individualizar la inscripción registral de la hipoteca que se extingue, y consignar la voluntad irrevocable de cancelar el gravamen. El deudor hipotecario no necesita comparecer por ser un acto liberatorio a su favor.",
        "distractors_analysis": "La Opción A es incorrecta porque la cancelación es otorgada unilateralmente por el titular del gravamen (el banco), no requiriéndose la comparecencia del deudor. La Opción C y D exigen formalidades inexistentes en la práctica notarial y registral del CNR.",
        "difficulty": "Media"
    },
    {
        "category_id": "notariado_puro",
        "question": "Un notario salvadoreño es designado y juramentado formalmente como Juez de Primera Instancia de lo Civil y Mercantil en la República. Conforme al régimen de incompatibilidades establecido taxativamente en el Art. 4 de la Ley de Notariado, ¿puede dicho funcionario continuar ejerciendo el notariado en su tiempo libre o durante los fines de semana?",
        "option_a": "Sí, siempre que no autorice escrituras sobre casos o litigios sometidos a su tribunal judicial.",
        "option_b": "No; el ejercicio de la judicatura con jurisdicción es incompatible de manera absoluta con el ejercicio de la función notarial, quedando en suspenso su facultad de cartular mientras dure en sus funciones judiciales.",
        "option_c": "Sí, pero requiere autorización escrita previa firmada por el Presidente de la Corte Suprema de Justicia.",
        "option_d": "Sí, pero únicamente para actos de jurisdicción voluntaria no contenciosa.",
        "correct_option": "B",
        "legal_basis": "Ley de Notariado, Art. 4 numeral 1° y Art. 5.",
        "justification": "El Art. 4 numeral 1° de la Ley de Notariado establece una incompatibilidad radical y absoluta: 'Se prohíbe el ejercicio de la función notarial a los que tienen autoridad o jurisdicción en los ramos judicial o de hacienda, en cualquier lugar de la República'. Todo juez de primera instancia, magistrado de cámara o de la CSJ está terminantemente impedido de ejercer el notariado, sin excepción de días ni materias.",
        "distractors_analysis": "Las opciones A, C y D intentan relativizar una incompatibilidad legal que en El Salvador es de orden público estricto. Cartular siendo juez con jurisdicción constituye falta gravísima sujeta a sanción de suspensión e inhabilitación por Corte Plena.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "notariado_puro",
        "question": "Un notario autoriza una escritura matriz de donación de un inmueble. Por un descuido material, el notario omite expresar la hora y el lugar del otorgamiento en la cabeza de la escritura. ¿Qué sanción o efecto jurídico produce esta omisión sobre dicho instrumento público según el Art. 32 y 33 de la Ley de Notariado?",
        "option_a": "No produce ningún efecto invalidante si las partes reconocen sus firmas ante el Juez de Paz.",
        "option_b": "El instrumento matriz adolece de nulidad absoluta, pues el lugar y la fecha son solemnidades esenciales exigidas por el Art. 32 de la Ley de Notariado para la existencia y validez del documento notarial.",
        "option_c": "Produce únicamente una multa administrativa de cincuenta colones impuesta por la Sección del Notariado, pero el contrato conserva plena validez jurídica.",
        "option_d": "Puede subsanarse mediante una simple certificación que el notario agregue al testimonio.",
        "correct_option": "B",
        "legal_basis": "Ley de Notariado, Art. 32 ordinal 1° y Art. 33; Código Civil Art. 1551.",
        "justification": "El Art. 32 ordinal 1° de la Ley de Notariado señala expresamente como primer requisito formal de la escritura matriz: 'El número de orden que le corresponda, el lugar, hora, día, mes y año en que se otorgue'. El Art. 33 de la misma ley sanciona con nulidad el instrumento cuando se omiten los requisitos formales solemnes de ley que determinan la certeza temporal y territorial de la fe pública.",
        "distractors_analysis": "La Opción A es incorrecta porque la nulidad de un instrumento público por falta de solemnidades esenciales no es saneable por ratificación judicial posterior. La Opción C confunde la sanción puramente disciplinaria con la ineficacia estructural del instrumento público (nulidad instrumental). La Opción D es ilícita conforme al Art. 35 LN.",
        "difficulty": "Media"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "En unas diligencias notariales de Aceptación de Herencia, transcurridos quince días desde la tercera publicación del edicto en el Diario Oficial sin que nadie comparezca a deducir derechos hereditarios ni a aceptar la herencia, ¿cuál es el paso legal que debe ordenar el notario conforme al Art. 22 de la LENJVOD?",
        "option_a": "Adjudicar los bienes hereditarios a la Universidad de El Salvador y a los Hospitales de la República en un solo acto.",
        "option_b": "Declarar yacente la herencia, nombrar un curador de la misma previa juramentación legal, y ordenar la publicación del nombramiento de conformidad con la ley.",
        "option_c": "Archivar las diligencias de forma definitiva sin emitir ninguna providencia.",
        "option_d": "Declarar heredero de oficio al Estado a través del Fiscal General de la República.",
        "correct_option": "B",
        "legal_basis": "LENJVOD, Art. 22; Código Civil, Art. 1164.",
        "justification": "El Art. 22 de la LENJVOD dispone que transcurridos quince días desde la última publicación del edicto sin que nadie se hubiere presentado a aceptar la herencia, el notario declarará yacente la herencia y nombrará un curador que la represente, a quien juramentará legalmente, y mandará a publicar este nombramiento en la forma prevista por la ley. Posteriormente, si transcurre el término de ley sin herederos, los bienes se transfieren según las reglas de sucesión legal del Código Civil.",
        "distractors_analysis": "La Opción A confunde la herencia yacente con la liquidación definitiva y asignación final al Estado y beneficiarios legales. La Opción C es denegación de trámite. La Opción D omite la fase obligatoria de declaración de yacencia y designación de curador.",
        "difficulty": "Media"
    },
    {
        "category_id": "civil_sucesiones",
        "question": "En un testamento solemne cerrado otorgado ante notario salvadoreño, ¿cuántos testigos instrumentales idóneos deben concurrir obligatoriamente a la presentación y otorgamiento de la carátula y pliego testamentario?",
        "option_a": "Tres testigos idóneos.",
        "option_b": "Cinco testigos instrumentales idóneos.",
        "option_c": "Siete testigos presenciales.",
        "option_d": "No requiere testigos si el notario sella el sobre con su sello oficial y lacre.",
        "correct_option": "B",
        "legal_basis": "Código Civil de El Salvador, Art. 1006.",
        "justification": "El Art. 1006 del Código Civil salvadoreño dispone taxativamente que el testamento solemne cerrado debe otorgarse ante Notario y CINCO TESTIGOS idóneos. En la cubierta del sobre que contiene el pliego testamentario cerrado, el notario extiende la carátula o acta de otorgamiento haciendo constar que el testador declaró de viva voz que el pliego contiene su testamento, firmando el testador, el notario y los cinco testigos.",
        "distractors_analysis": "La Opción A (tres testigos) corresponde al testamento abierto ante notario (Art. 996 C.C.), no al testamento cerrado. La Opción C es un número erróneo. La Opción D infringe las solemnidades esenciales del acto testamentario.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "mercantil_societario",
        "question": "En una escritura de Constitución de Sociedad de Responsabilidad Limitada (Ltda.) en El Salvador, ¿cuál es el número máximo de socios que la ley mercantil salvadoreña permite que participen válidamente en dicha persona jurídica?",
        "option_a": "No existe límite máximo de socios en ninguna sociedad mercantil.",
        "option_b": "El número de socios no puede ser mayor de veinticinco.",
        "option_c": "El número de socios no puede exceder de diez.",
        "option_d": "El número de socios no puede exceder de cincuenta.",
        "correct_option": "B",
        "legal_basis": "Código de Comercio de El Salvador, Art. 101.",
        "justification": "El Art. 101 del Código de Comercio salvadoreño establece con toda claridad que ninguna sociedad de responsabilidad limitada puede constituirse ni funcionar con más de VEINTICINCO SOCIOS. Si por cualquier motivo llegase a exceder de este número, la sociedad debe transformarse en sociedad anónima dentro del plazo legal so pena de disolución.",
        "distractors_analysis": "La Opción A aplica para las Sociedades Anónimas de capital, no para las de Responsabilidad Limitada. Las opciones C y D citan números incorrectos ajenos a la norma salvadoreña.",
        "difficulty": "Media"
    },
    {
        "category_id": "registral_cnr",
        "question": "Un notario autoriza una escritura pública de Donación entre vivos de un bien raíz a favor de un menor de 12 años de edad. En la escritura, el padre del menor comparece aceptando la donación en nombre y representación de su hijo. Al calificar el documento, el Registrador del CNR inscribe el derecho de propiedad sin objeción. ¿Es conforme a derecho esta actuación notarial y registral?",
        "option_a": "No, porque toda donación a favor de menores requiere autorización judicial previa con intervención de la Procuraduría General de la República.",
        "option_b": "Sí; de conformidad con el Código Civil, las donaciones a favor de incapaces o menores de edad pueden ser válidamente aceptadas por sus representantes legales (padres en ejercicio de la autoridad parental), ya que es un acto netamente adquisitivo y favorable al patrimonio del menor.",
        "option_c": "No, el menor de edad debe comparecer personalmente y estampar su huella dactilar asistido de un curador ad-litem.",
        "option_d": "No, porque las donaciones de inmuebles solo pueden realizarse a favor de mayores de edad con capacidad civil plena.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Art. 1282 y Código de Familia Art. 206 y ss.",
        "justification": "Conforme al Art. 1282 del Código Civil salvadoreño, las donaciones entre vivos hechas a personas incapaces o menores de edad no requieren autorización judicial previa si se trata de adquisiciones puras y simples (sin gravamen oneroso directo impuesto al menor), pudiendo ser aceptadas válidamente por sus representantes legítimos en ejercicio de la autoridad parental o tutela.",
        "distractors_analysis": "La Opción A confunde la enajenación o gravamen de bienes de menores (que sí exige autorización judicial previa conforme al Art. 230 C.F.) con la mera adquisición patrimonial por donación pura. La Opción C y D desconocen las reglas de representación legal de menores en el derecho civil y familiar salvadoreño.",
        "difficulty": "Media"
    },
    {
        "category_id": "notariado_puro",
        "question": "¿En cuál de los siguientes casos la Ley de Notariado de El Salvador faculta al notario a protocolizar un documento privado sin necesidad de previa resolución judicial?",
        "option_a": "Cuando se trate de un contrato de arrendamiento privado que las partes de mutuo acuerdo soliciten al notario protocolizar para dotarlo de fecha cierta.",
        "option_b": "Cuando se trate de un documento que transfiera el dominio de bienes raíces otorgado en documento privado simple.",
        "option_c": "Cuando se trate de un pagaré mercantil en mora para ejecutar judicialmente al deudor.",
        "option_d": "En El Salvador los documentos privados nunca pueden protocolizarse ante notario sin orden judicial de juez competente.",
        "correct_option": "A",
        "legal_basis": "Ley de Notariado, Art. 55 y Art. 56.",
        "justification": "El Art. 55 de la Ley de Notariado autoriza expresamente la protocolización de documentos por mandato de ley, por resolución judicial, o a solicitud de los interesados. Cuando las partes que han suscrito un documento privado (como un contrato de arrendamiento o acuerdo privado lícito) convienen en que se protocolice, el notario transcribe o inserta literalmente dicho documento en su libro de protocolo o lo anexa a él según el Art. 56 LN, confiriéndole fecha cierta y custodia institucional.",
        "distractors_analysis": "La Opción B es ilícita porque la compraventa de bienes raíces es un contrato solemne que no puede originarse válidamente en documento privado para luego protocolizarse (Art. 1605 C.C.). La Opción C es incorrecta porque el pagaré es un título valor cuya fuerza ejecutiva emana de sí mismo y no requiere protocolización. La Opción D es falsa.",
        "difficulty": "Media"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "En unas diligencias notariales de Aceptación de Herencia, ¿en qué momento procesal está obligado el notario a librar informe y oficio a la Secretaría General de la Corte Suprema de Justicia (Sección de Notariado)?",
        "option_a": "Únicamente cuando ya haya dictado la resolución final definitiva declarando herederos.",
        "option_b": "Inmediatamente después de autorizar el acta inicial en que tiene por aceptada la solicitud y admite a trámite las diligencias, para que la CSJ informe si no se ha promovido trámite judicial o notarial idéntico sobre la misma sucesión o si existe testamento.",
        "option_c": "Solo si uno de los interesados se lo pide por escrito en el expediente notarial.",
        "option_d": "El notario no tiene obligación de enviar informes a la CSJ durante las diligencias de herencia.",
        "correct_option": "B",
        "legal_basis": "LENJVOD, Art. 19 inciso 1° y disposiciones reglamentarias de la Corte Plena de la CSJ.",
        "justification": "El Art. 19 de la LENJVOD y la normativa de la Corte Plena de la CSJ exigen que al iniciar las diligencias de aceptación de herencia, el notario debe librar oficio a la Secretaría de la CSJ solicitando informe oficial sobre si en los registros consta la apertura de otras diligencias de la misma sucesión (evitando trámites dobles fraudulentos) o la existencia de testamentos otorgados por el causante. La resolución definitiva no puede pronunciarse sin que conste agregado el informe favorable de la CSJ.",
        "distractors_analysis": "La Opción A es incorrecta porque librar el informe al final vulneraría la seguridad jurídica; debe ser previo a la declaratoria provisional y definitiva. Las opciones C y D desconocen la obligación legal imperativa del notario frente a la CSJ.",
        "difficulty": "Media"
    },
    {
        "category_id": "civil_sucesiones",
        "question": "Un testador salvadoreño otorga testamento abierto dejando todos sus bienes a favor de su sobrino favorito. Al momento de fallecer, sobrevive su cónyuge no divorciada, quien carece absolutamente de bienes propios, rentas o profesión para subsistir. Conforme a las asignaciones forzosas del Código Civil, ¿qué derecho patrimonial asiste a la cónyuge sobreviviente?",
        "option_a": "Ninguno, pues en El Salvador rige el principio de libertad absoluta de testar y el testador eligió a su sobrino.",
        "option_b": "Tiene derecho a reclamar la Porción Conyugal legal íntegra (la cuarta parte del acervo sucesorio), que es una asignación forzosa que el testador estaba obligado a hacer y que la ley suple si fue preterida o excluida.",
        "option_c": "El testamento completo queda revocado automáticamente y se abre la sucesión intestada.",
        "option_d": "Tiene derecho a que el sobrino le pague una indemnización por daño moral.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Art. 1172, Art. 1173 y Art. 1177.",
        "justification": "El Art. 1172 del Código Civil define la Porción Conyugal como la parte del patrimonio de una persona difunta que la ley asigna al cónyuge sobreviviente que carece de lo necesario para su congrua subsistencia. Conforme al Art. 1177 C.C., la porción conyugal es la cuarta parte de los bienes del difunto. Al ser una asignación forzosa de orden público legal, tiene prelación sobre las disposiciones voluntarias testamentarias a favor del sobrino.",
        "distractors_analysis": "La Opción A es incorrecta porque la libertad testamentaria salvadoreña está expresamente limitada por las asignaciones forzosas (Art. 1172 C.C.). La Opción C es incorrecta porque el testamento no es nulo ni se revoca totalmente; se reforma judicialmente en lo necesario para pagar la porción conyugal forzosa. La Opción D carece de fundamento sucesorio.",
        "difficulty": "Media"
    },
    {
        "category_id": "familia_menores",
        "question": "En un poder general judicial con cláusulas especiales otorgado ante notario para ser utilizado ante los Tribunales de Familia y Civiles de El Salvador, ¿cuál de las siguientes facultades requiere mención especial y taxativa de conformidad con el Art. 69 del Código Procesal Civil y Mercantil (CPCM)?",
        "option_a": "La facultad de presentar la demanda inicial y ofrecer prueba documental.",
        "option_b": "La facultad de renunciar a la acción, transigir, someter a arbitraje, allanarse y recibir pagos en nombre del poderdante.",
        "option_c": "La facultad de comparecer a la audiencia preparatoria.",
        "option_d": "La facultad de sustituir el poder a favor de otro abogado colegiado.",
        "correct_option": "B",
        "legal_basis": "Código Procesal Civil y Mercantil (CPCM), Art. 69.",
        "justification": "El Art. 69 del CPCM distingue con absoluta precisión entre las facultades generales del procurador y las facultades que requieren cláusula especial taxativa en el poder. Se requiere otorgamiento expreso y específico para: renunciar, transigir, someter a arbitraje, allanarse, conciliar, interponer recursos extraordinarios de casación y recibir pagos directos o percibir sumas dinerarias en juicio.",
        "distractors_analysis": "Las facultades de las opciones A y C son generales y van implícitas en el poder general judicial sin necesidad de cláusula especial (Art. 67 y 68 CPCM). La sustitución requiere facultad pero la lista esencial de actos dispositivos materiales la define el Art. 69.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "notariado_puro",
        "question": "Un notario extravía cinco hojas de su libro de protocolo en blanco debido a un hurto en su despacho. ¿Cuál es el procedimiento legal inmediato que debe seguir de acuerdo con la Ley de Notariado?",
        "option_a": "Comprar cinco hojas nuevas en cualquier librería y sellarlas con su sello notarial.",
        "option_b": "Continuar cartulando en las hojas restantes y avisar hasta que concluya el año de vigencia del libro.",
        "option_c": "Dar aviso inmediatamente por escrito a la Sección del Notariado de la CSJ y presentar la denuncia penal respectiva en la Fiscalía General de la República (FGR), solicitando la reposición legal correspondiente de las hojas de conformidad con el trámite de ley.",
        "option_d": "Cerrar el protocolo en ese momento sin dar parte a ninguna autoridad para evitar sanciones disciplinarias.",
        "correct_option": "C",
        "legal_basis": "Ley de Notariado, Arts. 26 y 27.",
        "justification": "El protocolo es de estricto interés público y propiedad estatal. De conformidad con la Ley de Notariado y las instrucciones de la Sección del Notariado de la CSJ, el extravío, hurto o deterioro de hojas de protocolo exige dar aviso inmediato a la CSJ y formular la denuncia ante la FGR para deslindar responsabilidades por eventual mal uso de la fe pública, iniciando las diligencias de reposición de protocolo previstas en la ley.",
        "distractors_analysis": "La Opción A es delictiva (falsedad y alteración de sellos oficiales de Hacienda). Las opciones B y D conllevan responsabilidad disciplinaria gravísima y suspensión del ejercicio del notariado por omisión de custodia diligente.",
        "difficulty": "Fácil"
    }
]

FLASHCARDS = [
    {
        "category_id": "notariado_puro",
        "title": "Plazo para devolver el Libro de Protocolo",
        "prompt": "¿Dentro de qué plazo debe el notario entregar su libro de protocolo a la Sección del Notariado tras haber concluido el año de vigencia o haberse agotado las hojas?",
        "legal_answer": "Dentro de los QUINCE DÍAS siguientes al vencimiento del año o a la fecha en que se hubiere agotado el libro.",
        "legal_article": "Ley de Notariado, Art. 24"
    },
    {
        "category_id": "notariado_puro",
        "title": "Testigos Instrumentales Obligatorios",
        "prompt": "¿En qué casos es obligatoria la presencia de testigos instrumentales en el otorgamiento de una escritura matriz?",
        "legal_answer": "1. En los testamentos y donaciones por causa de muerte.\n2. Cuando alguno de los otorgantes no sepa o no pueda firmar (2 testigos).\n3. Cuando alguno de los otorgantes sea ciego, sordo o mudo.\n4. Cuando el notario o los otorgantes lo soliciten expresamente.",
        "legal_article": "Ley de Notariado, Art. 34; Código Civil, Art. 996"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "title": "Publicación de Edictos de Aceptación de Herencia",
        "prompt": "¿Cuántas veces y en qué medios deben publicarse los edictos de aceptación de herencia en sede notarial?",
        "legal_answer": "Tres veces en el Diario Oficial y tres veces en uno de los diarios de mayor circulación nacional.",
        "legal_article": "LENJVOD, Art. 19 inciso 2°"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "title": "Efecto de la Oposición en Jurisdicción Voluntaria",
        "prompt": "¿Qué debe hacer el notario si en cualquier estado de las diligencias de jurisdicción voluntaria se presenta oposición por un interesado?",
        "legal_answer": "Cesa de inmediato la función notarial en el asunto. El notario debe abstenerse de continuar y remitir las actuaciones originales al Juez de Primera Instancia competente.",
        "legal_article": "LENJVOD, Art. 2 (Principio de Consentimiento Unánime)"
    },
    {
        "category_id": "familia_menores",
        "title": "Plazo para remitir testimonio de Matrimonio",
        "prompt": "¿Cuál es el plazo fatal para que el notario remita el testimonio del acta matrimonial a la alcaldía municipal?",
        "legal_answer": "Dentro de los QUINCE DÍAS HÁBILES siguientes a la celebración del matrimonio.",
        "legal_article": "Código de Familia, Art. 28; LENJVOD, Art. 14"
    },
    {
        "category_id": "civil_sucesiones",
        "title": "Testigos en Testamento Abierto vs Cerrado",
        "prompt": "¿Cuántos testigos instrumentales se requieren para el testamento abierto y cuántos para el testamento cerrado ante notario?",
        "legal_answer": "Testamento Abierto: TRES (3) testigos idóneos.\nTestamento Cerrado: CINCO (5) testigos instrumentales idóneos.",
        "legal_article": "Código Civil, Art. 996 y Art. 1006"
    },
    {
        "category_id": "registral_cnr",
        "title": "Plazo de Subsanación en el CNR",
        "prompt": "¿Cuál es el término para retirar y subsanar un instrumento observado en el Registro de la Propiedad Raíz e Hipotecas antes de que caduque el asiento de presentación?",
        "legal_answer": "TREINTA DÍAS HÁBILES contados a partir del día siguiente a la notificación de la esquela u observación registral.",
        "legal_article": "Reglamento de la Ley de Reestructuración Registral, Art. 21"
    },
    {
        "category_id": "mercantil_societario",
        "title": "Capital Mínimo y Pago Inicial en S.A.",
        "prompt": "¿Cuál es el capital social mínimo para constituir una S.A. en El Salvador y el porcentaje mínimo a pagar en efectivo al momento del otorgamiento?",
        "legal_answer": "Capital mínimo: DOS MIL DÓLARES ($2,000.00).\nPago mínimo inicial al constituir: CINCO POR CIENTO (5%) de cada acción pagadera en numerario.",
        "legal_article": "Código de Comercio, Art. 192 numeral II"
    }
]
