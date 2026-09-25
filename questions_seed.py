"""
Banco de datos de casos prácticos y preguntas de alto nivel para el Examen
de Suficiencia para el Ejercicio de la Función Notarial de la Corte Suprema de Justicia (CSJ) de El Salvador.

Fundamentación rigurosa con base en:
- Ley de Notariado (LN)
- Ley del Ejercicio Notarial de la Jurisdicción Voluntaria y de Otras Diligencias (LENJVOD)
- Código Civil de El Salvador (C.C.)
- Código de Familia (C.F.)
- Ley Crecer Juntos (Protección Integral de la Primera Infancia, Niñez y Adolescencia)
- Código Procesal Civil y Mercantil (CPCM)
- Código de Comercio (C.Com.)
- Ley de Reestructuración Registral y Catastro (CNR)
- Ley Especial Reguladora de la Emisión del DUI y Ley de Reestructuración Municipal
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
        "description": "Matrimonio en sede notarial, regímenes patrimoniales, divorcio, salidas del país y poderes familiares.",
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
    # =========================================================================
    # --- 1. LEY DE NOTARIADO Y FUNCIÓN NOTARIAL (15 CASOS) ---
    # =========================================================================
    {
        "category_id": "notariado_puro",
        "question": "Comparece ante un notario salvadoreño una persona de 35 años que desea otorgar una donación irrevocable de un inmueble. Al solicitarle su documento de identidad, el otorgante manifiesta que extravió su Documento Único de Identidad (DUI) hace dos días y exhibe únicamente su Pasaporte Salvadoreño vigente y su Licencia de Conducir. ¿Puede el notario autorizar la escritura matriz con tales documentos de identificación?",
        "option_a": "Sí, porque el pasaporte es un documento oficial con fotografía emitido por el Estado que acredita la identidad de cualquier ciudadano salvadoreño.",
        "option_b": "No; tratándose de salvadoreños en el territorio de la República, el único documento legal para identificarse ante notario es el DUI, salvo que el notario lo conozca personalmente o se recurra a dos testigos de conocimiento.",
        "option_c": "Sí, siempre y cuando el notario relacione la Licencia de Conducir y agregue copia certificada de la misma al legajo de anexos del protocolo.",
        "option_d": "No, el notario debe suspender el acto de inmediato y no puede bajo ninguna circunstancia celebrar el instrumento hasta que el otorgante tramite su nuevo DUI.",
        "correct_option": "B",
        "legal_basis": "Ley de Notariado, Art. 32 ord. 5° y Ley Especial Reguladora de la Emisión del Documento Único de Identidad (DUI).",
        "justification": "De conformidad con el Art. 32 ord. 5° de la Ley de Notariado, el notario debe dar fe del conocimiento de los comparecientes. Si no los conoce personalmente, debe identificarlos por medio de su Documento de Identidad personal. Tratándose de salvadoreños mayores de edad domiciliados en la República, el DUI es el único documento legalmente idóneo para acreditar identidad civil; el pasaporte solo es admisible para salvadoreños residentes en el extranjero o extranjeros. No obstante, si el otorgante carece de DUI en el momento, la ley notarial salvadoreña faculta expresamente al notario a suplir la falta mediante dos testigos de conocimiento que conozcan al compareciente y sean conocidos del notario, o si el notario mismo lo conoce personalmente.",
        "distractors_analysis": "La Opción A es incorrecta porque la jurisprudencia de la CSJ y la normativa del DUI establecen que el pasaporte salvadoreño no sustituye al DUI para actos solemnes dentro del país. La Opción C es incorrecta porque la licencia de conducir no constituye documento de identidad notarial idóneo. La Opción D es incorrecta porque olvida la figura del conocimiento personal o los dos testigos de conocimiento conforme al Art. 32 ord. 5° LN.",
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
        "distractors_analysis": "La Opción A es incorrecta porque omite la firma a ruego y la concurrencia imperativa de testigos instrumentales (Art. 34 LN). La Opción B es incorrecta porque inventa la figura de un 'abogado asistente' no contemplada en la Ley de Notariado y reduce erróneamente los testigos a uno solo. La Opción D es un error conceptual grave: el analfabeto es plenamente capaz civilmente.",
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
        "distractors_analysis": "La Opción A es incorrecta porque la retención del libro agotado durante el resto del año está expresamente prohibida. La Opción C es incorrecta porque en El Salvador no se agregan hojas a un libro ya formado y agotado. La Opción D confunde la custodia del protocolo; los protocolos son del Estado.",
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
        "justification": "El Art. 9 de la Ley de Notariado prohíbe de manera terminante al notario autorizar instrumentos en que resulte o pueda resultar algún provecho directo para él, para su cónyuge, o para sus ascendientes, descendientes o hermanos, o sus parientes dentro del cuarto grado de consanguinidad o segundo de afinidad. El Art. 10 sanciona los instrumentos autorizados en contravención al Art. 9 con la nulidad absoluta de los mismos.",
        "distractors_analysis": "La Opción B es incorrecta porque el notario ejerce fe pública 24/7 en cualquier día y hora. La Opción C es incorrecta porque el notario tiene fe pública en toda la República. La Opción D es incorrecta porque el Art. 44 LN faculta la expedición de ulteriores testimonios.",
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
        "justification": "De acuerdo con el Art. 35 y 36 de la Ley de Notariado, una vez firmado el instrumento por los otorgantes y autorizado por el notario, este no puede alterar, enmendar ni agregar texto al instrumento matriz. Las enmendaduras y testaduras solo son válidas si se salvan al final del instrumento y ANTES de las firmas. Toda modificación posterior exige el otorgamiento de una nueva escritura matriz de rectificación o aclaración.",
        "distractors_analysis": "Las Opciones A y C son erróneas: las notas de salvatura posteriores a las firmas son nulas y constituyen falta grave de alteración del protocolo. La Opción D es incorrecta porque un acta notarial por separado no puede enmendar una escritura de protocolo.",
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
        "justification": "El Art. 50 de la Ley de Notariado establece expresamente que en las actas notariales se consignarán los hechos y actos que el notario presencie o que ante él se ejecuten o pasen, pero prohíbe tajantemente autorizar en actas notariales contratos y actos jurídicos solemnes que deban celebrarse en escritura matriz. La promesa de venta de un inmueble es un contrato formal y solemne que exige escritura pública matriz para su plena validez jurídica.",
        "distractors_analysis": "Las opciones A, B y D son actos formalizados mediante Acta Notarial según los Arts. 50 y 51 LN y las leyes mercantiles (protesto en acta, notificación en acta y comprobación de hechos materiales presenciados).",
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
        "justification": "El Art. 4 numeral 1° de la Ley de Notariado establece una incompatibilidad radical y absoluta: 'Se prohíbe el ejercicio de la función notarial a los que tienen autoridad o jurisdicción en los ramos judicial o de hacienda, en cualquier lugar de la República'. Todo juez de primera instancia o magistrado está terminantemente impedido de ejercer el notariado.",
        "distractors_analysis": "Las opciones A, C y D intentan relativizar una incompatibilidad legal que en El Salvador es de orden público estricto. Cartular siendo juez constituye falta gravísima sujeta a suspensión e inhabilitación por Corte Plena.",
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
        "distractors_analysis": "La Opción A es incorrecta porque la nulidad de un instrumento público por falta de solemnidades esenciales no es saneable por ratificación judicial posterior. La Opción C confunde la sanción disciplinaria con la ineficacia estructural. La Opción D es ilícita conforme al Art. 35 LN.",
        "difficulty": "Media"
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
        "justification": "El protocolo es de estricto interés público y propiedad estatal. De conformidad con la Ley de Notariado y las instrucciones de la Sección del Notariado de la CSJ, el extravío, hurto o deterioro de hojas de protocolo exige dar aviso inmediato a la CSJ y formular la denuncia ante la FGR para deslindar responsabilidades, iniciando las diligencias de reposición de protocolo previstas en la ley.",
        "distractors_analysis": "La Opción A es delictiva (falsedad y alteración de sellos oficiales de Hacienda). Las opciones B y D conllevan responsabilidad disciplinaria gravísima y suspensión del ejercicio del notariado por omisión de custodia diligente.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "notariado_puro",
        "question": "En la redacción de una escritura pública matriz, el notario consigna las cantidades del precio de venta y las fechas en guarismos o números arábigos ('$45,000.00' y '14/05/2024') sin escribirlos en letras completas, y utiliza abreviaturas corrientes como 'S.A.' y 'DUI'. ¿Cuál es la regla expresa del Art. 32 ord. 2° de la Ley de Notariado al respecto?",
        "option_a": "Está permitido el uso de cifras y abreviaturas en todo el instrumento siempre que sean de uso universal.",
        "option_b": "En las escrituras matrices y actas de protocolo está rigurosamente prohibido el uso de cifras o guarismos y de abreviaturas, debiendo escribirse todas las palabras, fechas, cantidades y menciones íntegramente en letras.",
        "option_c": "Se permiten cifras únicamente en el encabezado y en el precio, pero no en las cláusulas de descripción del inmueble.",
        "option_d": "El notario solo está obligado a escribir en letras los nombres de los otorgantes.",
        "correct_option": "B",
        "legal_basis": "Ley de Notariado, Art. 32 ordinal 2°.",
        "justification": "El Art. 32 ord. 2° de la Ley de Notariado establece como solemnidad imperativa: 'Que las escrituras se redacten en idioma castellano y que no se usen en ellas abreviaturas ni guarismos o números, aun para las fechas y cantidades, las cuales se escribirán íntegramente en letras'. Su infracción es objeto de constantes observaciones registrales y sanciones disciplinarias.",
        "distractors_analysis": "Las opciones A, C y D contradicen la prohibición taxativa y absoluta del Art. 32 ord. 2° LN, la cual busca prevenir adulteraciones materiales de cifras o confusiones en los instrumentos que custodian la propiedad raíz.",
        "difficulty": "Media"
    },
    {
        "category_id": "notariado_puro",
        "question": "Un notario autoriza una escritura matriz de compraventa de inmueble. Uno de los otorgantes firma y se retira; el segundo comparece cuatro días después a la oficina del notario a estampar su firma. El notario autoriza finalmente el instrumento con su firma y sello. ¿Qué vicio adolece esta escritura pública?",
        "option_a": "Ninguno, porque en los contratos bilaterales la ley permite que las partes firmen en días distintos mientras sea en el mismo mes.",
        "option_b": "Adolece de nulidad absoluta instrumental por infracción al principio de 'Unidad de Acto' consagrado en el Art. 32 ord. 10° y 13° de la Ley de Notariado, el cual exige lectura íntegra y otorgamiento simultáneo y continuo de las partes en un solo acto.",
        "option_c": "Solo genera una multa de 25 colones pero el instrumento es plenamente válido.",
        "option_d": "Es válida si el primer otorgante ratifica por teléfono su voluntad ante dos testigos.",
        "correct_option": "B",
        "legal_basis": "Ley de Notariado, Art. 32 ord. 10° y 13°; Jurisprudencia de la Sala de lo Civil de la CSJ.",
        "justification": "El principio notarial de Unidad de Acto exige que el otorgamiento, lectura y firma de la escritura matriz por todos los comparecientes ocurra en un solo acto continuado e ininterrumpido. La firma fraccionada en fechas o momentos sucesivos vulnera la esencia misma de la fe pública presencial del notario, originando la nulidad absoluta del instrumento público.",
        "distractors_analysis": "La Opción A es falsa doctrinaria y legalmente: no existe firma a plazos en el instrumento público salvadoreño. La Opción C confunde la sanción administrativa con la ineficacia sustancial del documento. La Opción D carece de toda base jurídica.",
        "difficulty": "Difícil"
    },
    {
        "category_id": "notariado_puro",
        "question": "¿Cuál es la consecuencia jurídica sobre el acto o contrato celebrado en una escritura pública cuando la escritura matriz es declarada NULA por haberse omitido formalidades solemnes de la Ley de Notariado (ejemplo: falta de testigos cuando un otorgante era ciego), según el Art. 62 de la Ley de Notariado?",
        "option_a": "El contrato de fondo queda nulo de pleno derecho y no puede ser convalidado ni probado de ninguna manera.",
        "option_b": "La nulidad del instrumento no produce necesariamente la del acto o contrato que contiene, el cual valdrá si se prueba por otros medios legales fehacientes o si consta en documento que tenga fuerza de instrumento privado.",
        "option_c": "Las partes deben ser multadas de inmediato por el Juez de lo Civil y el notario va a prisión automáticamente.",
        "option_d": "El Registro de la Propiedad inscribe el contrato como una posesión provisional.",
        "correct_option": "B",
        "legal_basis": "Ley de Notariado, Art. 62; Código Civil, Art. 1551 y Art. 1572.",
        "justification": "El Art. 62 de la Ley de Notariado establece una distinción fundamental entre el 'instrumento' (el continente formal) y el 'negocio jurídico' (el contenido sustantivo): 'La nulidad del instrumento no produce necesariamente la del acto o contrato que contiene, el cual valdrá si el acto o contrato no requiere de la escritura pública como solemnidad esencial ad substantiam y constare en forma que valga como documento privado'.",
        "distractors_analysis": "La Opción A desconoce el Art. 62 LN. Si la solemnidad era ad solemnitatem (como hipoteca o donación de inmueble), perece todo; pero si era ad probationem (como una fianza o venta mueble), el negocio sobrevive como documento privado. Las opciones C y D son absurdas.",
        "difficulty": "Experto"
    },
    {
        "category_id": "notariado_puro",
        "question": "Un notario salvadoreño que viaja a la ciudad de Milán, Italia, es requerido por dos salvadoreños para otorgar un poder general judicial y una escritura de compraventa de un inmueble situado en Santa Ana, El Salvador. Conforme a la Ley de Notariado, ¿tiene dicho notario facultad legal para autorizar tales escrituras matrices en el extranjero?",
        "option_a": "No, los notarios salvadoreños únicamente pueden cartular dentro de las fronteras territoriales de El Salvador.",
        "option_b": "Sí; los notarios salvadoreños pueden ejercer la función notarial en cualquier país extranjero para actos o contratos que deban surtir efectos en El Salvador, debiendo utilizar las hojas de su protocolo legalmente autorizado.",
        "option_c": "Solo puede autorizar poderes, pero bajo ninguna circunstancia compraventas o transferencias de dominio de inmuebles.",
        "option_d": "Solo puede autorizar si comparece como testigo el Cónsul salvadoreño acreditado en Milán.",
        "correct_option": "B",
        "legal_basis": "Ley de Notariado, Art. 3 inciso 2°.",
        "justification": "El Art. 3 inc. 2° de la Ley de Notariado salvadoreña consagra expresamente el principio de extraterritorialidad de la fe pública notarial: 'Los notarios podrán también ejercer sus funciones en países extranjeros, autorizando actos, contratos y declaraciones que hayan de surtir efecto en El Salvador'. El notario cartula en su propio protocolo asignado por la CSJ.",
        "distractors_analysis": "La Opción A es incorrecta porque la ley salvadoreña otorga extraterritorialidad expresa al notariado. La Opción C limita indebidamente el objeto de los actos (el Art. 3 no distingue entre poderes y compraventas). La Opción D exige formalidades consulares inexistentes para el notario salvadoreño.",
        "difficulty": "Media"
    },
    {
        "category_id": "notariado_puro",
        "question": "En relación con la foliación del libro de protocolo notarial, ¿cuál es el mandato imperativo de la Ley de Notariado sobre la numeración de las hojas y la correlatividad de las escrituras?",
        "option_a": "Las hojas del protocolo se folian en números al momento de encuadernar el libro, debiendo dejarse dos líneas en blanco entre cada escritura autorizada.",
        "option_b": "Las hojas del protocolo llevarán numeración correlativa en letras estampada por la Dirección General de Tesorería, y las escrituras se asentarán una a continuación de otra, sin dejar claros ni líneas en blanco, llevando numeración ordinal correlativa continua.",
        "option_c": "Cada escritura debe iniciar obligatoriamente en el anverso de una hoja nueva de protocolo.",
        "option_d": "El notario numera libremente las escrituras por año o por tipo de contrato a su criterio.",
        "correct_option": "B",
        "legal_basis": "Ley de Notariado, Arts. 16, 17 y 20.",
        "justification": "Conforme a los Arts. 16, 17 y 20 de la Ley de Notariado, las hojas vienen foliadas en letras por el Estado, y las escrituras deben extenderse una inmediatamente después de la otra, guardando estricta correlatividad numérica en orden de otorgamiento, sin intercalar hojas ni dejar espacios en blanco para evitar fraudes.",
        "distractors_analysis": "La Opción A y C son erróneas: no se dejan líneas ni se inicia obligatoriamente en hoja nueva; la escritura siguiente inicia a renglón seguido de la autorización anterior. La Opción D viola la numeración correlativa obligatoria.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "notariado_puro",
        "question": "¿En qué caso el notario salvadoreño está legalmente autorizado a extender un SEGUNDO TESTIMONIO de una escritura de mutuo con garantía hipotecaria a petición del acreedor hipotecario, sin necesidad de autorización judicial previa?",
        "option_a": "En ningún caso; cuando la escritura contenga una obligación pendiente de pago de dar o hacer, el segundo testimonio solo puede expedirse por orden de Juez competente previa justificación.",
        "option_b": "Siempre que el acreedor lo solicite por escrito y pague los derechos notariales correspondientes.",
        "option_c": "Únicamente si han transcurrido más de diez años desde el otorgamiento de la escritura matriz.",
        "option_d": "Cuando el deudor haya fallecido y la deuda sea hereditaria.",
        "correct_option": "A",
        "legal_basis": "Ley de Notariado, Art. 44 y Art. 45.",
        "justification": "El Art. 44 y 45 de la Ley de Notariado estatuye que si la escritura contiene obligaciones de dar o de hacer (como un mutuo hipotecario con saldo pendiente), el notario NO puede expedir nuevo testimonio a favor del acreedor sin mandato judicial del Juez de Primera Instancia, para evitar el riesgo de un doble cobro ejecutivo del mismo título contra el deudor.",
        "distractors_analysis": "Las opciones B, C y D desconocen la regla tuitiva del Art. 45 LN: la protección procesal del deudor frente a títulos ejecutivos duplicados exige intervención del juez para ordenar la expedición del segundo testimonio con fuerza ejecutiva.",
        "difficulty": "Experto"
    },

    # =========================================================================
    # --- 2. JURISDICCIÓN VOLUNTARIA NOTARIAL (LENJVOD) (14 CASOS) ---
    # =========================================================================
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
        "distractors_analysis": "La Opción A reduce ilegalmente las publicaciones a una. La Opción C confunde trámites judiciales. La Opción D omite el diario de circulación nacional, cuya omisión acarrea nulidad procesal y observación registral en el CNR.",
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
        "distractors_analysis": "Las opciones A y B son falsas porque el notario salvadoreño carece absolutamente de jurisdicción contenciosa. La Opción D vulnera el debido proceso y acarrea responsabilidad penal y civil.",
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
        "justification": "La citación legal de la totalidad de los colindantes es un requisito esencial de validez en las diligencias de remedición (Art. 15 LENJVOD). La falta de citación o la oposición de cualquiera de ellos a la mensura o a los linderos priva al notario de competencia, debiendo cesar en sus actuaciones y remitir el expediente al Juez de Primera Instancia.",
        "distractors_analysis": "La Opción A aplica erróneamente normas de emplazamiento judicial del CPCM ajenas al régimen consensual de la LENJVOD. La Opción C es ilegal. La Opción D es improcedente: el notario carece de imperio coactivo.",
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
        "justification": "Esta es una de las preguntas trampa clásicas del examen de notariado de la CSJ. La LENJVOD enumera taxativamente las diligencias que pueden seguirse ante notario. En ningún artículo facultó a los notarios para tramitar Títulos Supletorios. Conforme al Art. 699 C.C., la titulación supletoria es competencia estricta y privativa del Órgano Judicial.",
        "distractors_analysis": "Las opciones A, C y D confunden la titulación supletoria (exclusiva de jueces) con la remedición de inmuebles que ya cuentan con título inscrito (esta última sí atribuida a notarios por el Art. 15 LENJVOD).",
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
        "justification": "Conforme al Art. 11 y 12 de la LENJVOD, en las diligencias de rectificación de partidas de estado familiar, el notario practica las pruebas documentales y testimoniales en actas notariales fuera del protocolo; comprobado el error u omisión, dicta una resolución final y de ella expide testimonio o certificación notarial que remite al funcionario del Registro del Estado Familiar para su marginación.",
        "distractors_analysis": "La Opción A es incorrecta porque las diligencias no se otorgan en escritura matriz sino en expediente notarial de actas. La Opción C menciona una autoridad inconexa. La Opción D es ilícita.",
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
        "justification": "El Art. 22 de la LENJVOD dispone que transcurridos quince días desde la última publicación del edicto sin que nadie se hubiere presentado a aceptar la herencia, el notario declarará yacente la herencia y nombrará un curador que la represente, a quien juramentará legalmente, y mandará a publicar este nombramiento en la forma prevista por la ley.",
        "distractors_analysis": "La Opción A confunde la herencia yacente con la liquidación y adjudicación final al Estado. La Opción C es denegación indebida de trámite. La Opción D omite la fase obligatoria de declaración de yacencia y designación de curador.",
        "difficulty": "Media"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "¿En qué momento procesal debe el notario que tramita una Aceptación de Herencia solicitar el informe oficial a la Secretaría General de la Corte Suprema de Justicia respecto a si existen diligencias previas o testamentos registrados del causante?",
        "option_a": "Únicamente después de haber protocolizado la resolución definitiva de herederos.",
        "option_b": "Al inicio de las diligencias, inmediatamente después de proveída la solicitud y antes de emitir la declaratoria de heredero definitivo.",
        "option_c": "Solamente si se trata de sucesión testada, estando exonerado en la sucesión intestada.",
        "option_d": "El notario no rinde informe a la CSJ, solo a la Alcaldía Municipal.",
        "correct_option": "B",
        "legal_basis": "LENJVOD, Art. 19 inciso 1° y disposiciones reglamentarias de la Corte Plena de la CSJ.",
        "justification": "El Art. 19 de la LENJVOD y la normativa de la CSJ exigen que al iniciar las diligencias de aceptación de herencia, el notario libre oficio a la Secretaría General de la CSJ solicitando informe oficial sobre si en los registros consta la apertura de otras diligencias de la misma sucesión (evitando trámites dobles fraudulentos) o la existencia de testamentos del causante. La resolución definitiva no puede pronunciarse válidamente sin el informe de la CSJ.",
        "distractors_analysis": "La Opción A libraría el informe a destiempo vulnerando la seguridad jurídica. Las opciones C y D desconocen la obligación legal imperativa del notario frente al control de sucesiones de la CSJ.",
        "difficulty": "Media"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "En unas diligencias de Deslinde Voluntario de Inmuebles tramitadas ante notario conforme al Art. 16 de la LENJVOD, ¿cuál es el requisito formal indispensable para que la fijación de linderos produzca plena eficacia jurídica y pueda protocolizarse?",
        "option_a": "Que los propietarios colindantes manifiesten su consentimiento expreso y unánime en el acta de deslinde practicada por el notario y el perito agrimensor.",
        "option_b": "Que la resolución sea homologada previamente por la Cámara de Segunda Instancia.",
        "option_c": "Que se publiquen tres edictos en el Diario Oficial convocando a la Procuraduría General de la República.",
        "option_d": "Que el perito agrimensor sea empleado de la Dirección General del Instituto Geográfico Nacional.",
        "correct_option": "A",
        "legal_basis": "LENJVOD, Art. 16 en relación con el Art. 2.",
        "justification": "En el deslinde voluntario notarial (Art. 16 LENJVOD), la concordancia y avenimiento expreso de todos los colindantes es la base sustancial del acto. Si todos los colindantes aceptan la línea divisoria propuesta por el perito y constatada por el notario, se levanta el acta respectiva con sus firmas y se protocoliza en el protocolo del notario.",
        "distractors_analysis": "La Opción B exige una homologación judicial improcedente en actos no contenciosos. Las opciones C y D inventan formalidades y requisitos funcionariales que la LENJVOD no establece.",
        "difficulty": "Media"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "Una vez declarados definitivamente los herederos y vencidos los plazos de ley en unas diligencias de Aceptación de Herencia en sede notarial, ¿qué debe hacer el notario con la resolución final para que los herederos puedan inscribir sus bienes en el Registro de la Propiedad (CNR)?",
        "option_a": "Extender una simple fotocopia certificada de la última acta del expediente.",
        "option_b": "Protocolizar la resolución final en su libro de protocolo y expedir el correspondiente testimonio de protocolización a favor de los declarados herederos para su presentación al Registro.",
        "option_c": "Entregar el expediente original en papel simple al registrador de la propiedad.",
        "option_d": "Publicar un cuarto edicto en la radio nacional anunciando la adjudicación.",
        "correct_option": "B",
        "legal_basis": "LENJVOD, Art. 20; Ley de Reestructuración Registral.",
        "justification": "El Art. 20 de la LENJVOD ordena expresamente que pronunciada la declaratoria definitiva de herederos, el notario protocolizará dicha resolución final en su libro de protocolo corriente y expedirá testimonio a los interesados. Este testimonio de protocolización es el título inscribible en el Registro de la Propiedad Raíz e Hipotecas del CNR (Art. 686 C.C.).",
        "distractors_analysis": "La Opción A y C son inadmisibles en el CNR: los títulos inscribibles en El Salvador deben constar en testimonio de escritura matriz o testimonio de protocolización. La Opción D carece de fundamento normativo.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "Concluidas totalmente unas diligencias de jurisdicción voluntaria de Aceptación de Herencia o Remedición de Inmueble y expedidos los testimonios a los interesados, ¿cuál es el destino legal final que el notario debe darle al expediente original de las diligencias?",
        "option_a": "Debe incinerarlo en presencia de dos testigos para resguardar el secreto profesional.",
        "option_b": "Debe entregarlo a los clientes solicitantes para que lo conserven en su poder de forma perpetua.",
        "option_c": "Debe remitir el expediente original completo a la Sección de Notariado o al Archivo Judicial de la Corte Suprema de Justicia para su custodia permanente.",
        "option_d": "Debe conservarlo en su despacho privado sin rendir cuentas a ninguna institución.",
        "correct_option": "C",
        "legal_basis": "LENJVOD, Art. 24.",
        "justification": "El Art. 24 de la LENJVOD preceptúa que concluidas las diligencias y protocolizada la resolución final cuando corresponda, el notario remitirá el expediente original al archivo judicial correspondiente (Custodia Central de Expedientes de la CSJ), garantizando la fe pública y el control estatal de las actuaciones extrajudiciales.",
        "distractors_analysis": "La Opción A es un delito de destrucción de documentos oficiales. Las opciones B y D violan la obligación de depósito público impuesta por el Art. 24 LENJVOD.",
        "difficulty": "Media"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "En unas diligencias notariales para hacer constar la adecuación del nombre o rectificación por marginación de errores evidentes en una partida del Registro del Estado Familiar, ¿se requiere la publicación previa de edictos en el Diario Oficial?",
        "option_a": "Sí, siempre deben publicarse tres edictos por el principio de publicidad registral.",
        "option_b": "No; la rectificación por error material evidente o adecuación de nombre se tramita mediante acta notarial directa con la prueba documental pertinente, expidiéndose certificación para su marginación sin necesidad de edictos.",
        "option_c": "Solo se requiere edicto si el solicitante es una persona jurídica mercantil.",
        "option_d": "Requiere consulta vinculante al Tribunal Supremo Electoral.",
        "correct_option": "B",
        "legal_basis": "LENJVOD, Art. 11 y 12; Ley del Nombre de la Persona Natural, Arts. 23 y 24.",
        "justification": "A diferencia de la aceptación de herencia, las diligencias de rectificación de partidas y adecuación del nombre ante notario prescinden de la publicación de edictos, basándose en la comprobación documental directa de los asientos de estado familiar y el acta de comprobación notarial.",
        "distractors_analysis": "La Opción A confunde los requisitos de las sucesiones (Art. 19 LENJVOD) con el régimen sumario del nombre y estado familiar. Las opciones C y D carecen de sentido jurídico.",
        "difficulty": "Media"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "Un acreedor requiere a un notario salvadoreño para que notifique formalmente al deudor la cesión de un crédito hipotecario realizada a su favor, a fin de que la cesión surta efectos legales contra el deudor y terceros. ¿Qué instrumento notarial debe emplear el notario y cómo debe documentarlo conforme a la LENJVOD?",
        "option_a": "Debe otorgar una escritura matriz en su protocolo haciendo comparecer obligatoriamente al deudor.",
        "option_b": "Debe levantar un Acta Notarial fuera del protocolo en la que haga constar la notificación personal practicada al deudor, entregándole copia íntegra del título de crédito y de la cesión, devolviendo el acta original al acreedor.",
        "option_c": "Debe enviar un mensaje por correo electrónico certificado con firma electrónica simple.",
        "option_d": "El notario no puede practicar notificaciones; debe solicitarse obligatoriamente al Juzgado de lo Civil.",
        "correct_option": "B",
        "legal_basis": "LENJVOD, Art. 17; Código Civil, Art. 672 y Art. 1692.",
        "justification": "El Art. 17 de la LENJVOD faculta expresamente a los notarios para practicar notificaciones de cesiones de créditos, traspasos o revocatorias de mandatos. Se formaliza mediante Acta Notarial fuera del protocolo, entregando cédula o copia fehaciente al notificado.",
        "distractors_analysis": "La Opción A es incorrecta porque la notificación no exige comparecencia ni escritura matriz. La Opción C no cumple las formalidades notariales de la LENJVOD. La Opción D desconoce la facultad expresa notarial del Art. 17 LENJVOD.",
        "difficulty": "Media"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "¿Puede un notario salvadoreño tramitar y autorizar la Venta en Subasta Pública de un inmueble embargado en un juicio ejecutivo?",
        "option_a": "Sí, de conformidad con la ampliación de facultades de la jurisdicción voluntaria moderna.",
        "option_b": "No; los remates y subastas derivadas de embargos judiciales son actos de ejecución forzosa coercitiva que corresponden en exclusiva al Juez que conoce del proceso de ejecución.",
        "option_c": "Sí, siempre que el ejecutante y el ejecutado otorguen poder notarial conjunto.",
        "option_d": "Sí, si el avalúo pericial no excede de cincuenta mil dólares.",
        "correct_option": "B",
        "legal_basis": "Código Procesal Civil y Mercantil (CPCM), Art. 646 y siguientes; LENJVOD Art. 2.",
        "justification": "La subasta judicial de bienes embargados constituye un acto de ejecución forzosa de naturaleza netamente jurisdiccional y coercitiva (imperium). La LENJVOD prohíbe taxativamente la intervención notarial en actos contenciosos o de ejecución forzada de resoluciones judiciales.",
        "distractors_analysis": "Las opciones A, C y D desconocen la frontera indiscutible entre la jurisdicción voluntaria extrajudicial y los actos de ejecución forzosa reservados al juez competente (CPCM).",
        "difficulty": "Difícil"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "question": "En las diligencias notariales de aceptación de herencia, ¿puede comparecer un apoderado en representación de uno de los herederos para aceptar la herencia?",
        "option_a": "No, la aceptación de herencia es un acto personalísimo que no admite representación por poder.",
        "option_b": "Sí, siempre que el apoderado esté facultado mediante Poder General con Cláusula Especial o Poder Especial otorgado en escritura pública que mencione expresamente la facultad de aceptar la herencia respectiva.",
        "option_c": "Sí, basta una simple carta poder firmada por el heredero sin autenticar.",
        "option_d": "Sí, pero únicamente si el apoderado es pariente dentro del cuarto grado de consanguinidad del heredero.",
        "correct_option": "B",
        "legal_basis": "LENJVOD, Art. 18; Código Civil, Art. 1152; Código Procesal Civil y Mercantil, Art. 69.",
        "justification": "Conforme al Código Civil y la LENJVOD, la aceptación de herencia puede realizarse válidamente por apoderado especial o general con cláusula especial taxativa, debiendo constar el poder en escritura pública.",
        "distractors_analysis": "La Opción A es incorrecta porque la aceptación hereditaria sí admite representación voluntaria en El Salvador. La Opción C es ilegal (no se admiten cartas simples en sede notarial para actos dispositivos patrimoniales). La Opción D impone una limitación inexistente.",
        "difficulty": "Media"
    },

    # =========================================================================
    # --- 3. DERECHO CIVIL Y RÉGIMEN SUCESORIO (13 CASOS) ---
    # =========================================================================
    {
        "category_id": "civil_sucesiones",
        "question": "El testamento solemne abierto otorgado ante notario en El Salvador requiere para su validez la concurrencia obligatoria y presencial de:",
        "option_a": "Dos testigos presenciales de cualquier nacionalidad y mayores de 16 años.",
        "option_b": "Tres testigos instrumentales idóneos, que sepan leer y escribir, domiciliados en el lugar del otorgamiento, en un solo acto ininterrumpido.",
        "option_c": "Cinco testigos presenciales si el otorgamiento se realiza fuera de la capital de la República.",
        "option_d": "No requiere testigos instrumentales, bastando la fe pública del notario autorizante salvo que el testador sea analfabeto.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Art. 996 y Art. 999; Ley de Notariado, Art. 34 inciso 2°.",
        "justification": "Conforme al Art. 996 del Código Civil y Art. 34 inciso 2° de la Ley de Notariado, el testamento solemne abierto ante notario debe otorgarse ante TRES testigos instrumentales idóneos. Dicho acto debe realizarse en un solo contexto ininterrumpido (unidad de acto), con lectura en voz alta por el notario y presencia simultánea del testador y de los tres testigos de principio a fin.",
        "distractors_analysis": "La Opción A es incorrecta porque los testigos de testamento abierto ante notario deben ser tres y ser mayores de 18 años hábiles. La Opción C confunde las formalidades del testamento sin notario ante juez. La Opción D es falsa porque el testamento nunca prescinde de testigos instrumentales.",
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
        "distractors_analysis": "Las opciones A, C y D corresponden a personas legalmente hábiles para testificar en actos solemnes al no concurrir en ellas ninguna de las prohibiciones taxativas del Art. 999 C.C.",
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
        "justification": "Una particularidad fundamental del Derecho Civil salvadoreño es que El Salvador derogó las legítimas rigurosas y cuartas de mejoras hace más de un siglo. Rige un sistema de amplia libertad testamentaria, condicionado únicamente al cumplimiento de las asignaciones forzosas: los alimentos debidos por ley y la Porción Conyugal (Art. 1172 y ss. C.C.).",
        "distractors_analysis": "Las opciones A y C describen regímenes forzosos ajenos al Código Civil salvadoreño vigente. La Opción D es incorrecta porque el Código Civil contempla causales taxativas de desheredamiento de los asignatarios de alimentos (Art. 1121 C.C.).",
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
        "distractors_analysis": "La Opción A es incorrecta porque el exceso en el plazo no acarrea la nulidad del contrato traslaticio ni del pacto en sí, sino su reducción legal imperativa. La Opción C desconoce las normas de orden público del Art. 1683 C.C. La Opción D confunde figuras.",
        "difficulty": "Difícil"
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
        "distractors_analysis": "La Opción A es incorrecta porque la libertad testamentaria salvadoreña está limitada por las asignaciones forzosas (Art. 1172 C.C.). La Opción C es incorrecta porque el testamento no es nulo ni se revoca totalmente; se reforma judicialmente en lo necesario. La Opción D carece de fundamento sucesorio.",
        "difficulty": "Media"
    },
    {
        "category_id": "civil_sucesiones",
        "question": "Fallece una persona sin haber otorgado testamento (sucesión intestada). Al momento de abrirse la sucesión, le sobreviven su cónyuge no separado legalmente, sus dos hijos biológicos y su madre. De conformidad con el primer orden de sucesión intestada regulado en el Art. 988 del Código Civil salvadoreño, ¿cómo se distribuye legalmente la herencia?",
        "option_a": "La herencia se divide por partes iguales exclusivamente entre los dos hijos biológicos, quedando excluida la madre y el cónyuge.",
        "option_b": "La herencia se divide por partes iguales entre los dos hijos, el cónyuge sobreviviente y la madre, pues todos pertenecen al primer orden de suceder y concurren conjuntamente.",
        "option_c": "La madre recibe el 50% y los hijos se dividen el 50% restante.",
        "option_d": "El cónyuge recibe la totalidad de los bienes en usufructo universal vitalicio.",
        "correct_option": "B",
        "legal_basis": "Código Civil de El Salvador, Art. 988 ordinal 1°.",
        "justification": "El Art. 988 ord. 1° del Código Civil enumera a los llamados a la sucesión intestada en el primer orden: 'Los hijos, el padre, la madre y el cónyuge, y en su caso el conviviente en unión no matrimonial'. Todos ellos concurren simultáneamente y heredan por cabezas en cuotas iguales sobre la masa hereditaria.",
        "distractors_analysis": "La Opción A, C y D aplican criterios de legislaciones foráneas. En El Salvador, el primer orden sucesorio integra simultáneamente a hijos, padres y cónyuge por partes iguales.",
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
        "distractors_analysis": "La Opción A (tres testigos) corresponde al testamento abierto ante notario (Art. 996 C.C.), no al cerrado. La Opción C es un número erróneo. La Opción D infringe las solemnidades esenciales.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "civil_sucesiones",
        "question": "Dos copropietarios son dueños en común y proindiviso de un inmueble en cuotas del 50% cada uno. Uno de ellos decide vender su derecho proindiviso a un tercero extraño a la comunidad sin contar con el consentimiento del otro copropietario. ¿Es legalmente válido este contrato de compraventa autorizado por notario?",
        "option_a": "No; la venta de cosa proindivisa requiere indispensablemente el consentimiento unánime de todos los comuneros en escritura pública matriz.",
        "option_b": "Sí; cada comunero es dueño absoluto de su cuota o derecho proindiviso y puede transferirla, donarla o hipotecarla libremente sin requerir la autorización del otro copropietario.",
        "option_c": "Solo es válida si previamente se tramitan diligencias de partición extrajudicial.",
        "option_d": "Es válida pero debe constituirse forzosamente un usufructo a favor del copropietario que no vende.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Art. 2056 y Art. 1616.",
        "justification": "Conforme al Art. 2056 del Código Civil, cada comunero puede reivindicar su cuota, hipotecarla o enajenarla libremente por acto entre vivos o mortis causa. El comprador adquiere la calidad de comunero en la cuota transferida. El consentimiento unánime solo se requiere para actos materiales sobre la totalidad física del bien común, no para disponer del derecho ideal o cuota abstracta.",
        "distractors_analysis": "La Opción A confunde la venta del bien físico total con la enajenación de la cuota ideal. Las opciones C y D carecen de fundamento legal en el régimen de indivisión salvadoreño.",
        "difficulty": "Media"
    },
    {
        "category_id": "civil_sucesiones",
        "question": "En la constitución de una Hipoteca Abierta otorgada en escritura matriz ante notario por una persona natural a favor de una institución bancaria para garantizar obligaciones presentes y futuras, ¿cuáles son los dos elementos cuantitativos y temporales obligatorios que deben delimitarse para su validez e inscripción según el Código Civil y la Ley de Bancos?",
        "option_a": "No requiere límites de monto ni plazo; la hipoteca abierta es ilimitada por su propia naturaleza.",
        "option_b": "Debe determinarse con exactitud el monto máximo de capital garantizado y el plazo máximo de vigencia o duración de la garantía hipotecaria abierta.",
        "option_c": "Basta con señalar que garantiza 'todas las deudas pasadas, presentes y futuras' de por vida.",
        "option_d": "El plazo máximo legal jamás puede exceder de un año calendario.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Art. 2157; Ley de Bancos de El Salvador, Art. 217; Jurisprudencia Registral CNR.",
        "justification": "Por exigencia del principio de especialidad registral y la normativa bancaria y civil salvadoreña, la hipoteca abierta no puede constituirse en términos indeterminados u omnicomprensivos. Debe fijarse con precisión el MONTO MÁXIMO garantizado y el PLAZO DE VIGENCIA de la línea de crédito o garantía, requisitos sin los cuales el CNR suspende e inscribe con denegatoria.",
        "distractors_analysis": "Las opciones A y C violan el principio de especialidad registral (Arts. 2157 C.C. y CNR). La Opción D señala un plazo irrisorio que no aplica para líneas de crédito hipotecarias.",
        "difficulty": "Difícil"
    },
    {
        "category_id": "civil_sucesiones",
        "question": "Un vendedor transfiere un inmueble por un precio de diez mil dólares ($10,000.00). Al momento del otorgamiento, el justo precio comercial real de dicho bien raíz en el mercado ascendía a cincuenta mil dólares ($50,000.00). ¿Qué acción civil ordinaria asiste al vendedor según el Código Civil salvadoreño?",
        "option_a": "Acción pauliana o revocatoria por fraude a los acreedores.",
        "option_b": "Acción de rescisión del contrato de compraventa por Lesión Enorme, ya que el precio que recibió fue inferior a la mitad del justo precio de la cosa vendida.",
        "option_c": "Acción de nulidad absoluta por falta de consentimiento libre.",
        "option_d": "No tiene ninguna acción porque en materia de inmuebles no existe la lesión enorme en El Salvador.",
        "correct_option": "B",
        "legal_basis": "Código Civil de El Salvador, Arts. 1688, 1689 y 1690.",
        "justification": "El Art. 1689 del Código Civil establece que el vendedor sufre lesión enorme cuando el precio que recibe es inferior a la mitad del justo precio de la cosa que vende (en el caso: recibió $10,000 cuando el justo precio era $50,000; la mitad es $25,000). Esta acción prescribe en cuatro años (Art. 1696 C.C.) y aplica exclusivamente a compraventas de bienes raíces.",
        "distractors_analysis": "La Opción A aplica para fraude de acreedores, no desproporción de precio entre contratantes. La Opción C confunde lesión objetiva con vicios del consentimiento. La Opción D es falsa: la lesión enorme subsiste plenamente para inmuebles en el Código Civil salvadoreño.",
        "difficulty": "Media"
    },
    {
        "category_id": "civil_sucesiones",
        "question": "Conforme al Código Civil salvadoreño, ¿cuál es la solemnidad obligatoria para la constitución de una Servidumbre Voluntaria de Tránsito sobre un predio sirviente a favor de un predio dominante?",
        "option_a": "Puede constituirse verbalmente con la entrega de las llaves del portón de acceso.",
        "option_b": "Debe constituirse indispensablemente mediante Escritura Pública Matriz otorgada por los propietarios de ambos predios o sus apoderados con poder suficiente, e inscribirse en el Registro de la Propiedad Raíz correspondiente.",
        "option_c": "Basta con un acta notarial fuera de protocolo firmada por el dueño del predio sirviente.",
        "option_d": "Se constituye automáticamente por el uso pacífico durante seis meses.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Art. 822 y Art. 686 ord. 2°; Ley de Notariado, Art. 32.",
        "justification": "Las servidumbres voluntarias son gravámenes y derechos reales inmuebles. Conforme al Código Civil y la Ley de Notariado, su constitución exige el otorgamiento de Escritura Pública Matriz y su tradición se efectúa mediante la correspondiente inscripción en el Registro de la Propiedad Raíz e Hipotecas (CNR).",
        "distractors_analysis": "Las opciones A, C y D desconocen el carácter solemne y la exigencia de escritura matriz e inscripción registral para los derechos reales inmobiliarios en El Salvador.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "civil_sucesiones",
        "question": "Una persona dona irrevocablemente un inmueble a su sobrino mediante escritura pública autorizada por notario. Dos años más tarde, el donante comparece ante el mismo notario pretendiendo revocar unilateralmente la donación mediante otra escritura matriz, alegando que su sobrino ya no lo visita. ¿Puede el notario autorizar la revocación unilateral de dicha donación?",
        "option_a": "Sí, el donante puede revocar unilateralmente cualquier donación en cualquier tiempo.",
        "option_b": "No; las donaciones entre vivos (irrevocables) legalmente aceptadas y notificadas son irrevocables por la sola voluntad del donante, salvo rescisión por ingratitud declarada en sentencia judicial firme.",
        "option_c": "Sí, pero debe pagar una indemnización equivalente al 10% del valor del inmueble.",
        "option_d": "Sí, siempre que el sobrino no haya contraído matrimonio.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Arts. 1265, 1279 y 1299.",
        "justification": "Por definición legal (Art. 1265 C.C.), la donación entre vivos es un contrato solemne e irrevocable a título gratuito. Una vez aceptada por el donatario y autorizada en escritura pública, el donante no puede revocarla por su sola voluntad. La revocación por causal de ingratitud exige demanda contenciosa y sentencia judicial firme de tribunal competente.",
        "distractors_analysis": "La Opción A confunde la donación irrevocable entre vivos con las donaciones revocables mortis causa (que son asimiladas a testamentos). Las opciones C y D carecen de respaldo legal.",
        "difficulty": "Media"
    },
    {
        "category_id": "civil_sucesiones",
        "question": "En materia sucesoria salvadoreña, ¿cuál es el efecto jurídico si una persona que tiene asignatarios forzosos de alimentos otorga testamento instituyendo como único heredero universal a una fundación extranjera, omitiendo prever el pago de los alimentos debidos a sus hijos menores?",
        "option_a": "El testamento es nulo de nulidad absoluta en todas sus partes.",
        "option_b": "El testamento es válido en lo dispositivo, pero queda sujeto a la Acción de Reforma de Testamento para que se deduzca previamente del acervo hereditario la suma suficiente para cubrir las asignaciones forzosas de alimentos de ley.",
        "option_c": "La fundación extranjera pierde el 100% de la asignación a favor del Estado.",
        "option_d": "Los alimentos se extinguen con la muerte del causante sin excepción.",
        "correct_option": "B",
        "legal_basis": "Código Civil de El Salvador, Arts. 1186, 1187 y 1172.",
        "justification": "El Art. 1186 del Código Civil consagra la Acción de Reforma de Testamento, otorgada a los legitimarios y beneficiarios de asignaciones forzosas (alimentos y porción conyugal) a quienes el testador no les haya dejado lo que por ley les corresponde, a fin de que se reforme el testamento y se pague preferentemente su cuota legal.",
        "distractors_analysis": "La Opción A es incorrecta porque la omisión de asignaciones forzosas no produce la nulidad total del testamento sino su reforma judicial. La Opción D es falsa porque los alimentos legales adeudados constituyen baja general de la herencia que grava la masa sucesoria.",
        "difficulty": "Difícil"
    },

    # =========================================================================
    # --- 4. DERECHO DE FAMILIA Y MENORES (11 CASOS) ---
    # =========================================================================
    {
        "category_id": "familia_menores",
        "question": "Un notario salvadoreño autoriza un matrimonio civil en la ciudad de Santa Tecla el día 15 de marzo. De acuerdo con el mandato conjunto del Código de Familia y la LENJVOD, ¿cuál es el plazo fatal para que el notario remita el testimonio respectivo al Registro del Estado Familiar de la alcaldía correspondiente, y cuál es la consecuencia de omitirlo?",
        "option_a": "Tiene quince días hábiles contados a partir del siguiente al de la celebración; su omisión o retraso le acarrea responsabilidad administrativa y sanción de multa impuesta por la autoridad municipal.",
        "option_b": "Tiene un plazo indefinido mientras no se cierre su libro de protocolo anual.",
        "option_c": "Debe remitirlo dentro de los tres días siguientes únicamente a la Sección del Notariado de la CSJ.",
        "option_d": "El notario no tiene obligación de remitir testimonios; es carga exclusiva de los contrayentes.",
        "correct_option": "A",
        "legal_basis": "Código de Familia, Art. 28; LENJVOD, Art. 14; Ley Transitoria del Registro del Estado Familiar.",
        "justification": "El Art. 28 del Código de Familia y el Art. 14 de la LENJVOD ordenan al funcionario autorizante remitir testimonio del acta de matrimonio a la alcaldía municipal del lugar de celebración, y de los lugares de nacimiento de los cónyuges, dentro de los quince días hábiles siguientes al de la celebración del matrimonio. El retraso o incumplimiento acarrea multa impuesta por la municipalidad y responsabilidad disciplinaria.",
        "distractors_analysis": "La Opción B es falsa: el plazo de 15 días hábiles es perentorio. La Opción C confunde la alcaldía municipal con la Sección de Notariado. La Opción D contradice la naturaleza de la fe pública delegada.",
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
        "justification": "En la legislación salvadoreña, el divorcio donde existan hijos menores de edad no emancipados o personas dependientes debe ser decretado indispensablemente por un Juez de Familia (Art. 106 ord. 1° y Art. 108 Código de Familia), quien tiene el deber tutelar de velar por el interés superior del niño y aprobar judicialmente el convenio. Ningún notario puede autorizar un divorcio con menores.",
        "distractors_analysis": "La Opción A es una trampa muy común: la intervención o visto bueno de la PGR no habilita la sede notarial para disolver el matrimonio cuando hay menores. Las opciones C y D carecen de asidero legal.",
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
        "justification": "El Art. 41 del Código de Familia establece que a falta de capitulaciones matrimoniales o si estas resultaren ineficaces para determinar el régimen económico del matrimonio, se entenderá que los cónyuges quedan sujetos al régimen de COMUNIDAD DIFERIDA por ministerio de ley (régimen legal supletorio en El Salvador).",
        "distractors_analysis": "La Opción A (Separación de Bienes) y la Opción C (Participación en las Ganancias) solo aplican si las partes las pactan expresamente en escritura matriz. La Opción D es una figura derogada desde 1994.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "familia_menores",
        "question": "Una madre que ejerce la autoridad parental de su hijo de 8 años desea que el menor viaje al extranjero de vacaciones con sus tíos. El padre del menor reside legalmente en Estados Unidos. Conforme a la Ley Crecer Juntos (y normativa migratoria salvadoreña), ¿qué documento notarial debe otorgarse para autorizar la salida del país del niño?",
        "option_a": "Basta una carta simple firmada por la madre con copia de la partida de nacimiento del menor.",
        "option_b": "Debe otorgarse Acta Notarial o Escritura Pública de Autorización de Salida del País, otorgada por ambos padres (o por el padre en el extranjero ante Cónsul o Notario salvadoreño con apostilla), relacionando el destino, período de permanencia y los datos de la persona acompañante.",
        "option_c": "Se requiere una resolución del Ministerio de Relaciones Exteriores emitida en San Salvador.",
        "option_d": "La madre puede autorizar la salida por sí sola sin requerir el consentimiento del padre ausente.",
        "correct_option": "B",
        "legal_basis": "Ley Crecer Juntos, Art. 219 (anterior Art. 44 Ley de Protección Integral de la Niñez y Adolescencia - LEPINA/CONNA).",
        "justification": "Conforme al Art. 219 de la Ley Crecer Juntos y la Ley Especial de Migración y Extranjería, la salida de niñas, niños y adolescentes del país exige autorización notarial expresa de ambos progenitores en ejercicio de la autoridad parental. En el instrumento notarial debe determinarse con claridad el país de destino, la fecha de salida y regreso, y la identificación de la persona que viajará con el menor.",
        "distractors_analysis": "La Opción A no cumple los estándares solemnes notariales ni migratorios. La Opción D es contraria a la autoridad parental compartida. La Opción C menciona un trámite ajeno.",
        "difficulty": "Media"
    },
    {
        "category_id": "familia_menores",
        "question": "Un padre comparece ante notario otorgando una escritura pública matriz de Reconocimiento Voluntario de Hijo. Dos semanas después, el otorgante regresa a la oficina notarial solicitando otorgar una nueva escritura matriz para revocar y dejar sin efecto dicho reconocimiento, alegando que tiene dudas sobre su paternidad biológica. ¿Puede el notario autorizar la revocación?",
        "option_a": "Sí, porque todo acto otorgado en escritura pública puede ser revocado libremente mediante otro instrumento de igual jerarquía.",
        "option_b": "No; de conformidad con el Art. 143 del Código de Familia, el reconocimiento voluntario de un hijo es IRREVOCABLE de pleno derecho, aun cuando se haga en testamento y este sea revocado; cualquier impugnación de paternidad debe ventilarse en juicio contencioso ante el Juez de Familia.",
        "option_c": "Sí, siempre que comparezca la madre prestando su consentimiento expreso.",
        "option_d": "Sí, si el menor aún no ha cumplido un año de edad.",
        "correct_option": "B",
        "legal_basis": "Código de Familia de El Salvador, Art. 143.",
        "justification": "El Art. 143 del Código de Familia consagra el principio de irrevocabilidad absoluta del reconocimiento voluntario de paternidad: 'El reconocimiento es irrevocable, aun cuando se contenga en testamento y éste se revoque'. Ni el notario ni los otorgantes pueden dejar sin efecto un reconocimiento válidamente otorgado; la impugnación exige proceso judicial con prueba científica de ADN ante tribunal de familia.",
        "distractors_analysis": "Las opciones A, C y D desconocen la naturaleza indisponible y de orden público del estado familiar de filiación y el mandato tajante del Art. 143 C.F.",
        "difficulty": "Media"
    },
    {
        "category_id": "familia_menores",
        "question": "En la celebración solemne del Matrimonio Notarial en El Salvador, ¿cuáles son los artículos del Código de Familia que el notario autorizante está obligado por ley a dar lectura íntegra y en voz alta a los contrayentes durante el acto matrimonial?",
        "option_a": "Los artículos 11, 12, 14, 15, 16, 17, 18, 36 y 39 del Código de Familia.",
        "option_b": "Los artículos 100, 106 y 110 sobre causales de divorcio vincular.",
        "option_c": "Únicamente el artículo 1 del Código de Familia sobre los principios rectores de la familia.",
        "option_d": "Los artículos del Código Penal sobre el delito de bigamia y matrimonios ilegales.",
        "correct_option": "A",
        "legal_basis": "Código de Familia, Art. 27 inciso 2°.",
        "justification": "El Art. 27 inc. 2° del Código de Familia establece expresamente que durante la celebración del matrimonio, el funcionario (notario) dará lectura a los artículos 11, 12, 14, 15, 16, 17, 18, 36 y 39 de dicho cuerpo legal, que contienen la definición de matrimonio, aptitud nupcial, impedimentos y los derechos y deberes que nacen del matrimonio.",
        "distractors_analysis": "Las opciones B, C y D citan preceptos ajenos a la solemnidad ceremonial imperativa exigida por el Art. 27 C.F. para el otorgamiento del acta matrimonial.",
        "difficulty": "Difícil"
    },
    {
        "category_id": "familia_menores",
        "question": "Un padre y una madre que ejercen conjuntamente la autoridad parental de su hijo de 10 años desean vender una casa registrada a nombre del menor para invertir el dinero en la compra de un camión comercial para el negocio familiar. ¿Puede el notario autorizar la escritura matriz de compraventa directa del inmueble del menor?",
        "option_a": "Sí, porque los padres representan legalmente al menor y ejercen libre administración sobre su patrimonio.",
        "option_b": "No; los padres no pueden enajenar ni gravar bienes raíces propiedad de sus hijos menores de edad sin previa Autorización Judicial de Utilidad y Necesidad dictada por el Juez de Familia con audiencia de la PGR.",
        "option_c": "Sí, siempre que comparezca un tío del menor como testigo instrumental garantizando la inversión.",
        "option_d": "Sí, si el menor asiente verbalmente en el acta notarial.",
        "correct_option": "B",
        "legal_basis": "Código de Familia, Art. 230.",
        "justification": "El Art. 230 del Código de Familia prohíbe taxativamente a los padres enajenar o gravar bienes inmuebles pertenecientes a sus hijos menores sin que preceda autorización judicial de necesidad y utilidad calificada por Juez de Familia. Cualquier venta notarial otorgada sin este requisito judicial previo es absolutamente nula y rechazada de plano por el CNR.",
        "distractors_analysis": "La Opción A es incorrecta porque la patria potestad o autoridad parental no otorga facultades dispositivas irrestrictas sobre bienes raíces de menores. Las opciones C y D son jurídicamente ineficaces.",
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
        "justification": "El Art. 69 del CPCM distingue con absoluta precisión entre las facultades generales del procurador y las facultades que requieren cláusula especial taxativa en el poder. Se requiere otorgamiento expreso y específico para: renunciar, transigir, someter a arbitraje, allanarse, conciliar y recibir pagos directos o percibir sumas dinerarias en juicio.",
        "distractors_analysis": "Las facultades de las opciones A y C son generales y van implícitas en el poder sin necesidad de cláusula especial (Arts. 67 y 68 CPCM). La lista esencial de actos dispositivos materiales la define el Art. 69.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "familia_menores",
        "question": "En el otorgamiento de un Convenio de Divorcio por Mutuo Consentimiento en escritura pública ante notario (para ser presentado a sede judicial de familia), ¿cuál de las siguientes cláusulas es de inclusión OBLIGATORIA por mandato imperativo del Art. 108 del Código de Familia?",
        "option_a": "La renuncia a solicitar indemnización por daño moral.",
        "option_b": "La determinación sobre el cuidado personal de los hijos, el régimen de visitas y comunicación, la cuantía de la pensión alimenticia, las bases para su actualización y la garantía de su cumplimiento, así como el uso de la vivienda familiar y la pensión compensatoria si correspondiere.",
        "option_c": "La designación del albacea que liquidará la sociedad conyugal.",
        "option_d": "La obligación de los cónyuges de no volver a contraer matrimonio durante cinco años.",
        "correct_option": "B",
        "legal_basis": "Código de Familia, Art. 108.",
        "justification": "El Art. 108 del Código de Familia enumera de forma taxativa el contenido indispensable del convenio de divorcio: cuidado personal, régimen de visitas, cuota alimenticia con garantía, destino de la vivienda familiar y eventual pensión compensatoria. La omisión de cualquiera de estos puntos acarrea la inadmisibilidad de la solicitud en el juzgado de familia.",
        "distractors_analysis": "Las opciones A y D son cláusulas ilícitas o violatorias de derechos fundamentales. La Opción C confunde términos sucesorios con el régimen patrimonial familiar.",
        "difficulty": "Media"
    },
    {
        "category_id": "familia_menores",
        "question": "Una persona soltera de 28 años desea adoptar al hijo de 5 años de su difunta hermana. Comparecen los abuelos del menor ante notario a prestar su consentimiento en escritura pública de adopción. ¿Puede el notario autorizar la adopción directa del menor mediante escritura matriz?",
        "option_a": "Sí, de conformidad con la autonomía de la voluntad en la jurisdicción voluntaria.",
        "option_b": "No; en El Salvador toda adopción es estrictamente judicial y se rige por la Ley Especial de Adopciones con intervención de la Oficina de Adopciones del CONAPINA y del Juez Especializado de la Niñez; está prohibida la adopción directa en sede notarial.",
        "option_c": "Sí, siempre que el adoptante sea mayor en quince años respecto al adoptado.",
        "option_d": "Sí, pero requiere publicación de tres edictos en el Diario Oficial.",
        "correct_option": "B",
        "legal_basis": "Ley Especial de Adopciones de El Salvador; Código de Familia, Art. 165.",
        "justification": "La adopción en El Salvador es un proceso de orden público estatal reservado con exclusividad a la vía judicial especializada y al sistema administrativo de protección infantil (CONAPINA). Ningún notario puede autorizar instrumentos de adopción privada o directa.",
        "distractors_analysis": "Las opciones A, C y D intentan validar una figura que en El Salvador constituye fraude procesal e infracción grave a la Ley Especial de Adopciones.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "familia_menores",
        "question": "Durante la vigencia de un matrimonio celebrado bajo el régimen de Separación de Bienes, ambos cónyuges deciden cambiarlo voluntariamente al régimen de Comunidad Diferida. ¿Qué instrumento legal deben otorgar y qué trámite posterior es indispensable para que surta plenos efectos contra terceros?",
        "option_a": "Deben otorgar Escritura Pública Matriz de Capitulaciones Matrimoniales modificatorias y marginar el testimonio en las partidas de matrimonio y nacimiento de ambos cónyuges en el Registro del Estado Familiar.",
        "option_b": "Basta una declaración jurada ante la Defensoría del Consumidor.",
        "option_c": "El régimen patrimonial del matrimonio es inmutable y no puede modificarse una vez celebrado.",
        "option_d": "Deben divorciarse y volver a casarse al día siguiente.",
        "correct_option": "A",
        "legal_basis": "Código de Familia, Arts. 23, 85 y 86.",
        "justification": "El Art. 85 del Código de Familia permite expresamente la mutabilidad del régimen patrimonial del matrimonio durante la vida conyugal. Se otorga en escritura matriz de capitulaciones modificatorias y, para surtir efectos frente a terceros (Art. 86 C.F.), debe marginarse en el Registro del Estado Familiar.",
        "distractors_analysis": "La Opción C sostiene una tesis de inmutabilidad derogada desde 1994. Las opciones B y D son absurdas.",
        "difficulty": "Media"
    },

    # =========================================================================
    # --- 5. DERECHO MERCANTIL Y TÍTULOS VALORES (10 CASOS) ---
    # =========================================================================
    {
        "category_id": "mercantil_societario",
        "question": "Se constituye ante sus oficios notariales una Sociedad Anónima de Capital Variable (S.A. de C.V.) con un capital social pactado de VEINTE MIL DÓLARES. Conforme al Código de Comercio salvadoreño, ¿cuál es el porcentaje mínimo legal del capital social que debe pagarse efectivamente al momento del otorgamiento de la escritura de constitución?",
        "option_a": "Debe pagarse el cien por ciento (100%) mediante depósito bancario o cheque certificado.",
        "option_b": "Debe pagarse por lo menos el cinco por ciento (5%) de cada acción suscrita si es pagadera en dinero en efectivo.",
        "option_c": "Debe pagarse por lo menos el veinticinco por ciento (25%) del importe de cada acción pagadera en dinero efectivo.",
        "option_d": "Debe pagarse por lo menos el cincuenta por ciento (50%) en el acto y el resto en un plazo máximo de cinco años.",
        "correct_option": "B",
        "legal_basis": "Código de Comercio, Art. 192 numeral II.",
        "justification": "El Art. 192 numeral II del Código de Comercio de El Salvador establece expresamente que para la constitución de una sociedad anónima se requiere que el capital social no sea menor de dos mil dólares, y que si el capital se paga en dinero efectivo, se pague íntegramente por lo menos el CINCO POR CIENTO (5%) del valor de cada acción suscrita pagadera en numerario.",
        "distractors_analysis": "La Opción C (25%) era el régimen antiguo previo a las reformas de simplificación societaria. La Opción A aplica para el capital mínimo inicial cuando este sea de dos mil dólares pagados al 100% o aportes en especie. La Opción D carece de respaldo legal.",
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
        "justification": "Conforme al Art. 811 del Código de Comercio, el protesto de un cheque por falta de pago debe tener lugar antes de que expire el plazo de presentación (quince días naturales, Art. 808 C.Com.) o dentro de los tres días hábiles siguientes a la expiración de dicho plazo o de la fecha de la oportuna presentación.",
        "distractors_analysis": "La Opción B confunde el plazo de prescripción de la acción cambiaria con el plazo para levantar el protesto. La Opción C es un plazo ajeno. La Opción D es falsa: el protesto notarial subsiste.",
        "difficulty": "Difícil"
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
        "justification": "El Art. 101 del Código de Comercio salvadoreño establece con toda claridad que ninguna sociedad de responsabilidad limitada puede constituirse ni funcionar con más de VEINTICINCO SOCIOS. Si llegase a exceder de este número, la sociedad debe transformarse en sociedad anónima dentro del plazo legal so pena de disolución.",
        "distractors_analysis": "La Opción A aplica para las Sociedades Anónimas de capital. Las opciones C y D citan números incorrectos ajenos a la norma salvadoreña.",
        "difficulty": "Media"
    },
    {
        "category_id": "mercantil_societario",
        "question": "El administrador único de una Sociedad Anónima otorga un Poder General Judicial y Administrativo a favor de un abogado. Para que dicho poder pueda utilizarse eficazmente en trámites administrativos y judiciales representando a la sociedad, ¿es obligatoria su inscripción en el Registro de Comercio según el Art. 260 del Código de Comercio?",
        "option_a": "No, los poderes judiciales y administrativos otorgados por sociedades no se inscriben en el Registro de Comercio bajo ninguna circunstancia.",
        "option_b": "Sí; los poderes mercantiles otorgados por sociedades deben inscribirse obligatoriamente en el Registro de Comercio para que surtan plenos efectos y sea oponible frente a terceros la personería del mandatario.",
        "option_c": "Solo si el capital social de la sociedad excede de un millón de dólares.",
        "option_d": "Solo si el apoderado es de nacionalidad extranjera.",
        "correct_option": "B",
        "legal_basis": "Código de Comercio, Art. 260 y Art. 419 ord. 3°.",
        "justification": "Conforme al Art. 260 y Art. 419 ord. 3° del Código de Comercio, los poderes otorgados por comerciantes sociales (sociedades) deben inscribirse en el Registro de Comercio para acreditar formalmente la personería y representación legal frente a terceros, juzgados e instituciones públicas.",
        "distractors_analysis": "La Opción A confunde los poderes de personas naturales con los poderes mercantiles de sociedades. Las opciones C y D condicionan el registro a supuestos infundados.",
        "difficulty": "Media"
    },
    {
        "category_id": "mercantil_societario",
        "question": "Una Sociedad Anónima salvadoreña celebra Asamblea General Extraordinaria de Accionistas acordando un Aumento de Capital Social por la suma de cien mil dólares. ¿Cuál es la formalidad notarial indispensable para formalizar dicho acuerdo según el Art. 176 y 178 del Código de Comercio?",
        "option_a": "Basta con agregar el punto de acta al libro de actas de la sociedad sin intervención notarial.",
        "option_b": "El acuerdo de aumento de capital debe protocolizarse en Escritura Pública Matriz ante notario salvadoreño e inscribirse en el Registro de Comercio.",
        "option_c": "Basta con publicar un aviso en las redes sociales de la empresa.",
        "option_d": "El notario levanta un acta notarial fuera de protocolo y la remite al Ministerio de Hacienda.",
        "correct_option": "B",
        "legal_basis": "Código de Comercio, Art. 176, Art. 178 y Art. 22.",
        "justification": "Toda modificación del pacto social (incluido el aumento o disminución del capital social fijado en el pacto social) debe constar en Escritura Pública Matriz de modificación o protocolización de asamblea e inscribirse obligatoriamente en el Registro de Comercio para tener validez legal.",
        "distractors_analysis": "La Opción A no produce efectos frente a terceros ni modifica el pacto social registrado. Las opciones C y D violan la solemnidad de escritura pública matriz exigida por el Art. 22 C.Com.",
        "difficulty": "Media"
    },
    {
        "category_id": "mercantil_societario",
        "question": "En el endoso de una Letra de Cambio o Pagaré realizado con la cláusula 'Valor en Procuración' o 'Al Cobro', ¿qué facultades confiere el endosante al endosatario según el Código de Comercio salvadoreño?",
        "option_a": "Le transfiere la propiedad absoluta del título valor y de los fondos que representa.",
        "option_b": "No le transfiere la propiedad del título valor, pero faculta al endosatario para presentar el documento a la aceptación o al cobro judicial o extrajudicial, para protestarlo y para endosarlo únicamente en procuración.",
        "option_c": "Le faculta para donar el título valor o condonar la deuda al deudor principal.",
        "option_d": "Invalida el título valor por falta de tradición del dominio.",
        "correct_option": "B",
        "legal_basis": "Código de Comercio de El Salvador, Art. 662.",
        "justification": "El Art. 662 del Código de Comercio dispone que el endoso en procuración o al cobro no transmite la propiedad del título valor, sino que confiere un mandato mercantil especial para cobrar judicial o extrajudicialmente, otorgar recibos, protestar y endosar exclusivamente en procuración.",
        "distractors_analysis": "La Opción A describe el endoso en propiedad (Art. 656 C.Com.). Las opciones C y D contradicen la naturaleza del mandato de cobro cambiario.",
        "difficulty": "Media"
    },
    {
        "category_id": "mercantil_societario",
        "question": "¿Cuál es la consecuencia jurídica mercantil si una Sociedad Anónima constituida con un capital social pactado de dos mil dólares pierde más de las tres cuartas partes de dicho capital social según el Art. 187 numeral II del Código de Comercio?",
        "option_a": "La sociedad se disuelve de pleno derecho si los socios no reintegran el capital o limitan el fondo social a la parte existente dentro del plazo legal.",
        "option_b": "La sociedad se convierte automáticamente en una sociedad en comandita simple.",
        "option_c": "El Estado se convierte en accionista mayoritario al 51%.",
        "option_d": "No produce ninguna consecuencia mientras la sociedad continúe operando.",
        "correct_option": "A",
        "legal_basis": "Código de Comercio de El Salvador, Art. 187 numeral II.",
        "justification": "El Art. 187 num. II del Código de Comercio estatuye como causal legal de disolución de la sociedad anónima la pérdida de más de las tres cuartas partes del capital social, si los accionistas no lo reintegran o reducen legalmente el capital en asamblea extraordinaria.",
        "distractors_analysis": "Las opciones B, C y D carecen de base legal y contradicen las normas protectoras del capital social como garantía frente a terceros acreedores.",
        "difficulty": "Difícil"
    },
    {
        "category_id": "mercantil_societario",
        "question": "En una escritura de Constitución de Sociedad Mercantil, uno de los socios aporta en pago de su capital un bien inmueble. ¿Cómo debe formalizarse el pago de ese aporte en especie conforme a la Ley de Notariado y el Código de Comercio?",
        "option_a": "El inmueble debe estar totalmente pagado e integrarse el 100% en el acto constitutivo, describiéndose el inmueble, su antecedente registral, su valor pericial aprobado y haciéndose la tradición del dominio en la misma escritura matriz.",
        "option_b": "Basta con prometer transferir el inmueble dentro de los tres años siguientes a la constitución.",
        "option_c": "Los bienes inmuebles no pueden aportarse como capital a sociedades mercantiles salvadoreñas.",
        "option_d": "El inmueble se transfiere mediante acta notarial fuera del protocolo.",
        "correct_option": "A",
        "legal_basis": "Código de Comercio, Art. 195 y Art. 196; Ley de Notariado Art. 32.",
        "justification": "Conforme al Art. 195 y 196 del Código de Comercio, las aportaciones de bienes distintos del dinero (en especie) deben pagarse íntegramente (al 100%) al constituirse la sociedad, transfiriéndose la propiedad en la misma escritura constitutiva con todas las solemnidades registrales.",
        "distractors_analysis": "La Opción B es ilegal: las aportaciones no dinerarias no admiten pagos parciales aplazados. Las opciones C y D violan las normas societarias y registrales.",
        "difficulty": "Media"
    },
    {
        "category_id": "mercantil_societario",
        "question": "En el caso de fallecimiento de un socio en una Sociedad Colectiva mercantil salvadoreña, ¿qué regla aplica por mandato del Código de Comercio si el pacto social no estipula expresamente la continuación con los herederos?",
        "option_a": "La sociedad anónima sustituye a la colectiva de pleno derecho.",
        "option_b": "La muerte de uno de los socios colectivos disuelve la sociedad, a menos que en la escritura se haya pactado continuar con los herederos o con los socios sobrevivientes.",
        "option_c": "Los herederos asumen forzosamente la administración sin poder retirarse.",
        "option_d": "El capital del socio fallecido pasa a la Tesorería de la República.",
        "correct_option": "B",
        "legal_basis": "Código de Comercio de El Salvador, Art. 83 y Art. 84.",
        "justification": "Las sociedades colectivas son sociedades de personas fundadas en el principio 'intuitu personae'. La muerte de un socio produce por regla general la disolución de la sociedad, salvo pacto expreso en contrario en la escritura matriz constitutiva.",
        "distractors_analysis": "Las opciones A, C y D desconocen la naturaleza personalista de las sociedades colectivas salvadoreñas.",
        "difficulty": "Media"
    },
    {
        "category_id": "mercantil_societario",
        "question": "Para autorizar la Escritura Pública de Fusión de dos Sociedades Anónimas en El Salvador, ¿cuál es el requisito de publicidad previo que exige el Código de Comercio antes del otorgamiento solemne?",
        "option_a": "Publicar el acuerdo de fusión y el balance de las sociedades tres veces en el Diario Oficial y tres veces en un diario de mayor circulación, para permitir el derecho de oposición de los acreedores.",
        "option_b": "Publicar un aviso en la página web de una de las sociedades durante 24 horas.",
        "option_c": "No requiere publicidad si ambas sociedades están solventes con la alcaldía.",
        "option_d": "Solicitar autorización a la Corte Suprema de Justicia.",
        "correct_option": "A",
        "legal_basis": "Código de Comercio de El Salvador, Art. 317 y Art. 318.",
        "justification": "Los Arts. 317 y 318 del Código de Comercio ordenan publicar los acuerdos de fusión y el último balance general tres veces en el Diario Oficial y en un diario de mayor circulación, abriendo un plazo de noventa días para que los acreedores sociales ejerzan su derecho legal de oposición previa.",
        "distractors_analysis": "Las opciones B, C y D omiten el trámite protector de acreedores de los Arts. 317-318 C.Com., cuya inobservancia acarrea la nulidad de la inscripción registral de la fusión.",
        "difficulty": "Difícil"
    },

    # =========================================================================
    # --- 6. DERECHO REGISTRAL Y CATASTRO (CNR) (10 CASOS) ---
    # =========================================================================
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
        "category_id": "registral_cnr",
        "question": "Un notario autoriza una escritura pública de Donación entre vivos de un bien raíz a favor de un menor de 12 años de edad. En la escritura, el padre del menor comparece aceptando la donación en nombre y representación de su hijo. Al calificar el documento, el Registrador del CNR inscribe el derecho de propiedad sin objeción. ¿Es conforme a derecho esta actuación notarial y registral?",
        "option_a": "No, porque toda donación a favor de menores requiere autorización judicial previa con intervención de la Procuraduría General de la República.",
        "option_b": "Sí; de conformidad con el Código Civil, las donaciones a favor de incapaces o menores de edad pueden ser válidamente aceptadas por sus representantes legales (padres en ejercicio de la autoridad parental), ya que es un acto netamente adquisitivo y favorable que incrementa su patrimonio sin imponerle gravámenes.",
        "option_c": "No, porque el menor de 12 años debe firmar personalmente la escritura matriz con dos testigos instrumentales.",
        "option_d": "No, el donatario menor de edad no puede adquirir inmuebles por donación hasta cumplir la mayoría de edad.",
        "correct_option": "B",
        "legal_basis": "Código Civil de El Salvador, Art. 1279 inciso 2°.",
        "justification": "El Art. 1279 inc. 2° del Código Civil establece que las donaciones a favor de personas que no tienen la libre administración de sus bienes pueden ser válidamente aceptadas por sus representantes legales (padres o tutores). Al ser un acto puramente favorable que ingresa bienes libres al patrimonio del menor, no se requiere autorización judicial previa.",
        "distractors_analysis": "La Opción A confunde la adquisición favorable (donación pura) con la enajenación o gravamen de bienes de menores (que sí exige autorización judicial, Art. 230 C.F.). Las opciones C y D son jurídicamente falsas.",
        "difficulty": "Media"
    },
    {
        "category_id": "registral_cnr",
        "question": "En el Derecho Registral Inmobiliario salvadoreño, ¿en qué consiste el Principio de Tracto Sucesivo regulado en el Reglamento del Registro de la Propiedad Raíz e Hipotecas?",
        "option_a": "En que el primer documento que ingresa al Registro tiene prioridad sobre cualquier otro.",
        "option_b": "En que para inscribir un título traslaticio o modificativo del dominio de un inmueble, debe constar previamente inscrito el derecho de propiedad en cabeza de la persona que otorga la transferencia o afectación, formando una cadena ininterrumpida de titularidades.",
        "option_c": "En la obligación del registrador de despachar los documentos en un plazo de quince días.",
        "option_d": "En que las inscripciones nunca pueden ser canceladas por orden judicial.",
        "correct_option": "B",
        "legal_basis": "Reglamento de la Ley de Reestructuración del Registro de la Propiedad Raíz e Hipotecas, Art. 14.",
        "justification": "El Principio de Tracto Sucesivo (Art. 14 del Reglamento) exige una perfecta concatenación o encadenamiento ininterrumpido en el historial del inmueble: el otorgante del acto traslaticio debe coincidir exactamente con el titular que figura inscrito en el folio real o libro de propiedad.",
        "distractors_analysis": "La Opción A define el Principio de Prioridad Registral ('Prior tempore, potior jure'). Las opciones C y D definen plazos administrativos o violan el principio de tutela judicial efectiva.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "registral_cnr",
        "question": "Un propietario vende el mismo inmueble en la mañana a 'A' ante un notario, y en la tarde lo vende a 'B' ante otro notario. El comprador 'B' presenta su testimonio al CNR el día siguiente; el comprador 'A' lo presenta dos semanas después. ¿Quién adquiere el derecho de propiedad oponibilidad erga omnes frente al Registro según el Principio de Prioridad Registral?",
        "option_a": "El comprador 'A', porque su escritura se otorgó primero en orden cronológico horario.",
        "option_b": "El comprador 'B', porque su título fue el primero en ingresar y asentarse en el libro de presentación del Registro ('Primero en tiempo de presentación, primero en derecho').",
        "option_c": "Ambos compradores quedan como copropietarios proindivisos al 50%.",
        "option_d": "Ambas escrituras quedan nulas y el inmueble pasa al Estado.",
        "correct_option": "B",
        "legal_basis": "Código Civil, Art. 680; Reglamento de la Ley de Reestructuración Registral, Art. 12.",
        "justification": "En el sistema registral salvadoreño, la preferencia y oponibilidad real frente a terceros no se rige por la hora del otorgamiento notarial, sino por el momento del ingreso y asiento de presentación en el Registro de la Propiedad Raíz e Hipotecas (Principio de Prioridad o Rango Registral: Prior in tempore, potior in jure).",
        "distractors_analysis": "La Opción A confunde la fecha del negocio sustantivo con la prioridad registral. Las opciones C y D son incompatibles con el régimen de propiedad privada.",
        "difficulty": "Media"
    },
    {
        "category_id": "registral_cnr",
        "question": "Para inscribir en el CNR una escritura de Segregación por Cabeza de su Dueño de una porción de cinco mil metros cuadrados de un inmueble de mayor extensión, ¿cuál es el requisito técnico previo indispensable aprobado por el Instituto Geográfico y del Catastro Nacional (CNR-Catastro)?",
        "option_a": "La presentación del plano topográfico de la porción segregada y de la porción restante debidamente revisado y aprobado con su respectiva ficha catastral y coordenadas georreferenciadas.",
        "option_b": "Una fotografía aérea certificada por la Policía Nacional Civil.",
        "option_c": "La anuencia escrita de la Asamblea Legislativa de El Salvador.",
        "option_d": "Un estudio de impacto ambiental del Ministerio de Medio Ambiente para todo tipo de segregación rústica o urbana.",
        "correct_option": "A",
        "legal_basis": "Ley de Catastro y Normas Técnicas de Catastro del CNR; Art. 32 LN.",
        "justification": "De conformidad con la Ley de Catastro y la normativa del CNR, toda segregación inmobiliaria exige la aprobación catastral previa de los planos topográficos georreferenciados (tanto de la porción segregada como de la porción remanente o resto), debiendo el notario relacionar en la escritura la descripción técnica exacta de ambos polígonos aprobados.",
        "distractors_analysis": "Las opciones B, C y D exigen requisitos absurdos o inexistentes en el régimen registral y catastral ordinario de El Salvador.",
        "difficulty": "Fácil"
    },
    {
        "category_id": "registral_cnr",
        "question": "En una escritura matriz de Compraventa de Inmueble con Hipoteca, el notario incurre en el error material de consignar el número de matrícula registral como '30124567-00000' cuando el folio real correcto del inmueble era '30124576-00000'. Las partes ya firmaron y se autorizó el testimonio. ¿Cómo se subsana registralmente este error ante el CNR?",
        "option_a": "El notario acude al CNR y solicita al registrador que tache el número con tinta roja.",
        "option_b": "El notario, con la comparecencia de las partes otorgantes, otorga una nueva Escritura Pública Matriz de Aclaración o Rectificación en su protocolo, consignando la matrícula correcta y relacionando el antecedente, presentándola al CNR dentro del plazo de ley.",
        "option_c": "El comprador puede corregir el testimonio original a mano con corrector blanco.",
        "option_d": "El registrador de oficio investiga y cambia la matrícula sin necesidad de nuevo instrumento.",
        "correct_option": "B",
        "legal_basis": "Ley de Notariado, Art. 36; Reglamento del Registro de la Propiedad Raíz e Hipotecas, Art. 21 y Art. 48.",
        "justification": "Una vez firmada la escritura, el Art. 36 de la Ley de Notariado prohíbe alteraciones al texto original. La rectificación de errores sustanciales en la matrícula del inmueble exige otorgar una nueva escritura matriz de rectificación ante notario con comparecencia de los otorgantes.",
        "distractors_analysis": "Las opciones A y C constituyen ilícitos de alteración de documentos públicos. La Opción D es improcedente porque el registrador califica sobre el documento presentado sin alterar la voluntad matriz.",
        "difficulty": "Media"
    },
    {
        "category_id": "registral_cnr",
        "question": "¿En qué caso opera la figura de la Cancelación por Caducidad del gravamen hipotecario en el Registro de la Propiedad Raíz e Hipotecas (CNR) según la Ley de Reestructuración Registral?",
        "option_a": "A los dos años de inscrita si el banco no remite estados de cuenta.",
        "option_b": "Transcurridos treinta años desde el vencimiento del plazo estipulado en la obligación principal garantizada, siempre que no conste en el Registro interrupción de la prescripción ni demanda judicial de cobro anotada.",
        "option_c": "A los diez años contados desde la muerte del deudor hipotecario.",
        "option_d": "Las hipotecas inscritas en El Salvador nunca caducan por el transcurso del tiempo.",
        "correct_option": "B",
        "legal_basis": "Ley de Reestructuración del Registro de la Propiedad Raíz e Hipotecas, Art. 30; Código Civil Art. 2253.",
        "justification": "El Art. 30 de la Ley de Reestructuración Registral faculta la cancelación registral por caducidad de hipotecas sobre las cuales hayan transcurrido más de treinta años contados desde la fecha en que la obligación garantizada debió haberse cumplido en su totalidad, sin que conste anotación judicial de embargo o reclamo.",
        "distractors_analysis": "Las opciones A y C citan plazos erróneos. La Opción D es falsa: la legislación salvadoreña contempla la cancelación por caducidad para sanear inmuebles con hipotecas centenarias o prescritas.",
        "difficulty": "Difícil"
    },
    {
        "category_id": "registral_cnr",
        "question": "Un notario autoriza una escritura pública de Compraventa de Inmueble situado en el nuevo municipio de 'San Salvador Centro' (Distrito de San Salvador) tras la entrada en vigor de la Ley Especial de Reestructuración Municipal. ¿Cómo debe consignarse correctamente la ubicación municipal en el instrumento notarial para evitar observaciones registrales en el CNR?",
        "option_a": "Debe consignarse únicamente el nombre de la comarca sin mencionar el municipio ni el departamento.",
        "option_b": "Debe relacionarse la ubicación geográfica conforme a la nueva división político-administrativa: indicando el Municipio nuevo (ej. San Salvador Centro) y el Distrito correspondiente (ej. Distrito de San Salvador, Departamento de San Salvador).",
        "option_c": "Debe utilizarse exclusivamente la división territorial de 1939 para no contradecir el Código Civil.",
        "option_d": "Está prohibido consignar el distrito en los instrumentos de compraventa.",
        "correct_option": "B",
        "legal_basis": "Ley Especial de Reestructuración Municipal (Decreto Legislativo de los 44 Municipios); Criterios de Calificación CNR 2024-2026.",
        "justification": "Con la reforma que agrupó al país en 44 nuevos municipios divididos en Distritos, los criterios registrales del CNR exigen que los notarios identifiquen los inmuebles consignando el nuevo Municipio rector y el Distrito territorial correspondiente para asegurar la debida concordancia catastral y tributaria municipal.",
        "distractors_analysis": "La Opción A es deficiente. La Opción C desconoce la vigencia inmediata de la ley de reorganización territorial de orden público. La Opción D contradice la directriz registral.",
        "difficulty": "Media"
    },
    {
        "category_id": "registral_cnr",
        "question": "En el Registro de la Propiedad Raíz e Hipotecas (CNR), ¿cuál es el efecto jurídico principal del Asiento de Presentación respecto a otros títulos que ingresen posteriormente sobre el mismo inmueble?",
        "option_a": "No produce ningún efecto hasta que el registrador inscriba el documento de forma definitiva.",
        "option_b": "Bloquea temporalmente la inscripción de títulos incompatibles posteriores y otorga prelación temporal al documento presentado mientras esté vigente el plazo legal de calificación y subsanación.",
        "option_c": "Transfiere la posesión física inmediata del bien al notario autorizante.",
        "option_d": "Cancela automáticamente todos los embargos que pesaban sobre el inmueble.",
        "correct_option": "B",
        "legal_basis": "Reglamento del Registro de la Propiedad Raíz e Hipotecas, Arts. 12 y 13; Código Civil Art. 680.",
        "justification": "El asiento de presentación produce una reserva de prioridad y rango registral de efecto protector erga omnes: todo documento ingresado con posterioridad queda supeditado a la suerte del primero mientras este mantenga vigente su asiento de presentación.",
        "distractors_analysis": "La Opción A desconoce el efecto de prioridad procesal del asiento de presentación. Las opciones C y D carecen de fundamento legal.",
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
        "category_id": "notariado_puro",
        "title": "Prohibiciones por Parentesco del Notario",
        "prompt": "¿Cuáles son los grados de parentesco prohibidos para que el notario autorice escrituras en que resulte provecho?",
        "legal_answer": "Cónyuge, parientes dentro del CUARTO GRADO DE CONSANGUINIDAD (hijos, padres, hermanos, tíos, sobrinos, primos) o SEGUNDO DE AFINIDAD (suegros, yernos, nueras, cuñados). Su infracción acarrea NULIDAD ABSOLUTA.",
        "legal_article": "Ley de Notariado, Arts. 9 y 10"
    },
    {
        "category_id": "notariado_puro",
        "title": "Incompatibilidad Judicial con el Notariado",
        "prompt": "¿Pueden los jueces de primera instancia o magistrados con jurisdicción ejercer el notariado?",
        "legal_answer": "NO. El ejercicio de la judicatura con jurisdicción en cualquier ramo es incompatible de forma absoluta con la función notarial (prohibición radical de orden público).",
        "legal_article": "Ley de Notariado, Art. 4 numeral 1°"
    },
    {
        "category_id": "notariado_puro",
        "title": "Prohibición de Cifras y Abreviaturas",
        "prompt": "¿Pueden utilizarse abreviaturas o números en las escrituras matrices de protocolo?",
        "legal_answer": "NO. Está terminantemente prohibido el uso de abreviaturas y guarismos o cifras en las escrituras matrices; todas las palabras, fechas y cantidades deben constar íntegramente en letras.",
        "legal_article": "Ley de Notariado, Art. 32 ord. 2°"
    },
    {
        "category_id": "notariado_puro",
        "title": "Extraterritorialidad de la Fe Notarial",
        "prompt": "¿Pueden los notarios salvadoreños autorizar escrituras matrices en el extranjero?",
        "legal_answer": "SÍ. Pueden cartular en países extranjeros para actos y contratos que hayan de surtir efectos en El Salvador, utilizando su protocolo oficial.",
        "legal_article": "Ley de Notariado, Art. 3 inciso 2°"
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
        "category_id": "jurisdiccion_voluntaria",
        "title": "Títulos Supletorios e Incompetencia Notarial",
        "prompt": "¿Puede el notario tramitar y otorgar Títulos Supletorios?",
        "legal_answer": "NO. Las diligencias de titulación supletoria están reservadas en exclusiva a la vía judicial ante el Juez de Primera Instancia Civil (Art. 699 C.C.).",
        "legal_article": "Código Civil, Art. 699; LENJVOD"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "title": "Declaratoria de Herencia Yacente",
        "prompt": "¿Cuándo debe el notario declarar yacente la herencia en diligencias notariales?",
        "legal_answer": "Transcurridos quince días desde la tercera publicación del edicto sin que comparezca ningún heredero, el notario declara yacente la herencia y nombra curador.",
        "legal_article": "LENJVOD, Art. 22"
    },
    {
        "category_id": "jurisdiccion_voluntaria",
        "title": "Remedición de Inmuebles y Colindantes",
        "prompt": "¿Qué ocurre en la remedición de inmuebles si un colindante no es citado o formaliza oposición?",
        "legal_answer": "La falta de citación o la oposición de un colindante vicia el trámite extrajudicial, obligando al notario a cesar sus funciones y remitir el expediente al Juez.",
        "legal_article": "LENJVOD, Art. 15"
    },
    {
        "category_id": "civil_sucesiones",
        "title": "Testigos en Testamento Abierto vs Cerrado",
        "prompt": "¿Cuántos testigos instrumentales se requieren para el testamento abierto y cuántos para el testamento cerrado ante notario?",
        "legal_answer": "Testamento Abierto: TRES (3) testigos idóneos.\nTestamento Cerrado: CINCO (5) testigos instrumentales idóneos.",
        "legal_article": "Código Civil, Art. 996 y Art. 1006"
    },
    {
        "category_id": "civil_sucesiones",
        "title": "Porción Conyugal en El Salvador",
        "prompt": "¿A cuánto equivale la Porción Conyugal legal asignada al cónyuge sobreviviente sin bienes propios?",
        "legal_answer": "Equivale a la CUARTA PARTE (25%) del acervo ilíquido de los bienes del causante. Es asignación forzosa con prelación sobre asignaciones voluntarias.",
        "legal_article": "Código Civil, Arts. 1172 y 1177"
    },
    {
        "category_id": "civil_sucesiones",
        "title": "Primer Orden de Sucesión Intestada",
        "prompt": "¿Quiénes integran el primer orden de sucesión intestada en El Salvador según el Art. 988 C.C.?",
        "legal_answer": "Los hijos, el padre, la madre y el cónyuge (y en su caso el conviviente en unión no matrimonial declarada). Concurren simultáneamente por partes iguales.",
        "legal_article": "Código Civil, Art. 988 ordinal 1°"
    },
    {
        "category_id": "civil_sucesiones",
        "title": "Plazo Máximo del Pacto de Retroventa",
        "prompt": "¿Cuál es el plazo máximo legal permitido para la acción de retroventa en compraventas inmobiliarias?",
        "legal_answer": "CUATRO AÑOS contados desde la fecha del contrato. Cualquier plazo mayor estipulado por las partes se reduce de pleno derecho a 4 años.",
        "legal_article": "Código Civil, Art. 1683"
    },
    {
        "category_id": "civil_sucesiones",
        "title": "Lesión Enorme en Compraventa de Inmuebles",
        "prompt": "¿Cuándo sufre el vendedor lesión enorme en una compraventa de bienes raíces?",
        "legal_answer": "Cuando el precio que recibe es inferior a la mitad del justo precio del inmueble al momento del contrato. Prescribe en 4 años.",
        "legal_article": "Código Civil, Arts. 1688, 1689 y 1696"
    },
    {
        "category_id": "familia_menores",
        "title": "Plazo para remitir testimonio de Matrimonio",
        "prompt": "¿Cuál es el plazo fatal para que el notario remita el testimonio del acta matrimonial a la alcaldía municipal?",
        "legal_answer": "Dentro de los QUINCE DÍAS HÁBILES siguientes a la celebración del matrimonio.",
        "legal_article": "Código de Familia, Art. 28; LENJVOD, Art. 14"
    },
    {
        "category_id": "familia_menores",
        "title": "Régimen Patrimonial Supletorio Legal",
        "prompt": "¿Cuál es el régimen económico que rige el matrimonio salvadoreño por ministerio de ley a falta de capitulaciones?",
        "legal_answer": "El régimen de COMUNIDAD DIFERIDA.",
        "legal_article": "Código de Familia, Art. 41 y Art. 51"
    },
    {
        "category_id": "familia_menores",
        "title": "Prohibición de Divorcio Notarial con Menores",
        "prompt": "¿Puede el notario autorizar el divorcio si existen hijos menores de edad de por medio?",
        "legal_answer": "NO. Todo divorcio con hijos menores de edad o dependientes corresponde exclusivamente al Juez de Familia.",
        "legal_article": "Código de Familia, Arts. 106 ord. 1° y 108"
    },
    {
        "category_id": "familia_menores",
        "title": "Irrevocabilidad del Reconocimiento de Hijo",
        "prompt": "¿Puede un padre revocar ante notario un reconocimiento voluntario de hijo otorgado en escritura matriz?",
        "legal_answer": "NO. El reconocimiento es IRREVOCABLE de pleno derecho, aun cuando conste en testamento revocado.",
        "legal_article": "Código de Familia, Art. 143"
    },
    {
        "category_id": "familia_menores",
        "title": "Venta de Bienes Raíces de Menores",
        "prompt": "¿Pueden los padres vender un inmueble de sus hijos menores sin autorización de un juez?",
        "legal_answer": "NO. Se requiere indispensablemente Autorización Judicial previa de Utilidad y Necesidad dictada por el Juez de Familia con audiencia a la PGR.",
        "legal_article": "Código de Familia, Art. 230"
    },
    {
        "category_id": "mercantil_societario",
        "title": "Capital Mínimo y Pago Inicial en S.A.",
        "prompt": "¿Cuál es el capital social mínimo para constituir una S.A. en El Salvador y el porcentaje mínimo a pagar en efectivo al momento del otorgamiento?",
        "legal_answer": "Capital mínimo: DOS MIL DÓLARES ($2,000.00).\nPago mínimo inicial al constituir: CINCO POR CIENTO (5%) de cada acción pagadera en numerario.",
        "legal_article": "Código de Comercio, Art. 192 numeral II"
    },
    {
        "category_id": "mercantil_societario",
        "title": "Límite de Socios en Sociedad de Responsabilidad Limitada",
        "prompt": "¿Cuál es el número máximo de socios que pueden conformar una Sociedad de Responsabilidad Limitada (Ltda.)?",
        "legal_answer": "Máximo VEINTICINCO (25) socios.",
        "legal_article": "Código de Comercio, Art. 101"
    },
    {
        "category_id": "mercantil_societario",
        "title": "Plazo para Protesto Notarial de Cheques",
        "prompt": "¿Cuál es el plazo legal para levantar el protesto notarial por falta de pago de un cheque bancario?",
        "legal_answer": "Antes de expirar el plazo de presentación (15 días naturales) o dentro de los TRES DÍAS HÁBILES siguientes a su vencimiento o presentación.",
        "legal_article": "Código de Comercio, Art. 811"
    },
    {
        "category_id": "mercantil_societario",
        "title": "Registro de Poderes Mercantiles Societarios",
        "prompt": "¿Deben inscribirse los poderes mercantiles otorgados por sociedades en el Registro de Comercio?",
        "legal_answer": "SÍ. La inscripción en el Registro de Comercio es obligatoria para la plena oponibilidad de la personería del apoderado frente a terceros.",
        "legal_article": "Código de Comercio, Art. 260"
    },
    {
        "category_id": "registral_cnr",
        "title": "Plazo de Subsanación de Observaciones en el CNR",
        "prompt": "¿Cuál es el término para retirar y subsanar un instrumento observado en el Registro de la Propiedad Raíz e Hipotecas antes de que caduque el asiento de presentación?",
        "legal_answer": "TREINTA DÍAS HÁBILES contados a partir del día siguiente a la notificación de la esquela u observación registral.",
        "legal_article": "Reglamento de la Ley de Reestructuración Registral, Art. 21"
    },
    {
        "category_id": "registral_cnr",
        "title": "Principio de Prioridad Registral",
        "prompt": "¿Qué determina la preferencia erga omnes entre dos títulos traslaticios otorgados sobre el mismo inmueble?",
        "legal_answer": "El momento cronológico de ingreso y Asiento de Presentación en el Registro de la Propiedad ('Prior in tempore, potior in jure').",
        "legal_article": "Código Civil, Art. 680; Reglamento CNR, Art. 12"
    },
    {
        "category_id": "registral_cnr",
        "title": "Principio de Tracto Sucesivo",
        "prompt": "¿En qué consiste el principio registral de Tracto Sucesivo?",
        "legal_answer": "En la exigencia de que el derecho del otorgante conste previamente inscrito en el Registro, garantizando una cadena continua e ininterrumpida de titularidades.",
        "legal_article": "Reglamento de la Ley de Reestructuración Registral, Art. 14"
    },
    {
        "category_id": "registral_cnr",
        "title": "Cancelación de Hipoteca por Caducidad",
        "prompt": "¿Cuándo procede la cancelación registral por caducidad de una hipoteca en el CNR?",
        "legal_answer": "Transcurridos TREINTA AÑOS desde la fecha de vencimiento de la obligación garantizada sin que conste demanda judicial ni anotación preventiva.",
        "legal_article": "Ley de Reestructuración Registral, Art. 30"
    }
]
