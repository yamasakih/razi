import unittest

from sqlalchemy import select, func
from sqlalchemy import create_engine

from rdkit.Chem import AllChem as Chem

from razi.rdkit_postgresql.types import Mol


engine = create_engine('postgresql://localhost/razi-rdkit-postgresql-test')

class PropsTestCase(unittest.TestCase):

    def test_props(self):

        rs = engine.execute(select([ func.mol_amw(func.mol('c1ccccc1')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 78.114)

        rs = engine.execute(select([ func.mol_logp(func.mol('c1ccccc1')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 1.6866)

        rs = engine.execute(select([ func.mol_hba(func.mol('c1ccccc1')) ]))
        self.assertEqual(rs.fetchall()[0][0], 0)

        rs = engine.execute(select([ func.mol_hbd(func.mol('c1ccccc1')) ]))
        self.assertEqual(rs.fetchall()[0][0], 0)


        rs = engine.execute(select([ func.mol_chi0n(func.mol('c1ccccc1O')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 3.83396)

        rs = engine.execute(select([ func.mol_chi1n(func.mol('c1ccccc1O')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 2.13429)

        rs = engine.execute(select([ func.mol_chi2n(func.mol('c1ccccc1O')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 1.33555)

        rs = engine.execute(select([ func.mol_chi3n(func.mol('c1ccccc1O')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 0.756194)

        rs = engine.execute(select([ func.mol_chi4n(func.mol('c1ccccc1O')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 0.427994)


        rs = engine.execute(select([ func.mol_chi0v(func.mol('c1ccccc1O')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 3.83396)

        rs = engine.execute(select([ func.mol_chi1v(func.mol('c1ccccc1O')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 2.13429)

        rs = engine.execute(select([ func.mol_chi2v(func.mol('c1ccccc1O')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 1.33555)

        rs = engine.execute(select([ func.mol_chi3v(func.mol('c1ccccc1O')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 0.756194)

        rs = engine.execute(select([ func.mol_chi4v(func.mol('c1ccccc1O')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 0.427994)


        rs = engine.execute(select([ func.mol_kappa1(func.mol('C12CC2C3CC13')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 2.34375)

        rs = engine.execute(select([ func.mol_kappa2(func.mol('CC(C)C1CCC(C)CCC1')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 4.13265)

        rs = engine.execute(select([ func.mol_kappa3(func.mol('CC(C)C1CCC(C)CCC1')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 2.84444)


        rs = engine.execute(select([ func.mol_numspiroatoms(func.mol('CC1(C)CC2(C)CCC1(C)CC2')) ]))
        self.assertEqual(rs.fetchall()[0][0], 0)

        rs = engine.execute(select([ func.mol_numbridgeheadatoms(func.mol('CC1(C)CC2(C)CCC1(C)CC2')) ]))
        self.assertEqual(rs.fetchall()[0][0], 2)


        rs = engine.execute(select([ func.mol_formula(func.mol('[2H]C([3H])O')) ]))
        self.assertEqual(rs.fetchall()[0][0], 'CH4O')


        rs = engine.execute(select([ func.mol_numrotatablebonds(func.mol('CCCC')) ]))
        self.assertEqual(rs.fetchall()[0][0], 1)

        rs = engine.execute(select([ func.mol_numheavyatoms(func.mol('CCC')) ]))
        self.assertEqual(rs.fetchall()[0][0], 3)

        rs = engine.execute(select([ func.mol_numatoms(func.mol('CCC')) ]))
        self.assertEqual(rs.fetchall()[0][0], 11)

        rs = engine.execute(select([ func.mol_numheteroatoms(func.mol('CCO')) ]))
        self.assertEqual(rs.fetchall()[0][0], 1)


        rs = engine.execute(select([ func.mol_tpsa(func.mol('CCO')) ]))
        self.assertAlmostEqual(rs.fetchall()[0][0], 20.23)


        rs = engine.execute(select([ func.mol_numrings(func.mol('CCO')) ]))
        self.assertEqual(rs.fetchall()[0][0], 0)


        rs = engine.execute(select([ func.mol_murckoscaffold(func.mol('c1ccccc1CCO')) ]))
        self.assertEqual(rs.fetchall()[0][0], 'c1ccccc1')


        rs = engine.execute(select([ func.mol_to_svg(func.mol('CCO')) ]))
        self.assertEqual(rs.fetchall()[0][0], '''<?xml version='1.0' encoding='iso-8859-1'?>
<svg:svg version='1.1' baseProfile='full'
              xmlns:svg='http://www.w3.org/2000/svg'
                      xmlns:rdkit='http://www.rdkit.org/xml'
                      xmlns:xlink='http://www.w3.org/1999/xlink'
                  xml:space='preserve'
width='250px' height='200px' >
<svg:rect style='opacity:1.0;fill:#FFFFFF;stroke:none' width='250' height='200' x='0' y='0'> </svg:rect>
<svg:path d='M 11.3636,124.362 95.7545,75.6385' style='fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1' />
<svg:path d='M 95.7545,75.6385 131.455,96.25' style='fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1' />
<svg:path d='M 131.455,96.25 167.155,116.862' style='fill:none;fill-rule:evenodd;stroke:#FF0000;stroke-width:2px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1' />
<svg:text x='166.64' y='131.862' style='font-size:15px;font-style:normal;font-weight:normal;fill-opacity:1;stroke:none;font-family:sans-serif;text-anchor:start;fill:#FF0000' ><svg:tspan>OH</svg:tspan></svg:text>
</svg:svg>
''')

    maxDiff = None
